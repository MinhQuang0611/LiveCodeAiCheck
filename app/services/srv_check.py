
import logging
import os
import json
import psycopg
from copydetect import CopyDetector
from app.schemas.sche_check import UserSubmission, Problem, Report, PlagiarismCase
from app.core.config import settings

# Ngưỡng lọc
MIN_TOKEN_OVERLAP = 80
MIN_SIMILARITY_PERCENT = 60  # 60%


def fetch_submissions_from_db(base_dir: str):
    """
    Lấy dữ liệu StudentSubmissions từ PostgreSQL và lưu vào thư mục submissions.
    Returns: dict mapping problem_id -> list of student_ids
    """
    submissions = {}
    
    # logging.info(f"DB URL: {settings.DATABASE_URL}")

    try:
        with psycopg.connect(settings.DATABASE_DSN) as conn:
            with conn.cursor() as cur:
                # Lấy danh sách problem_id
                cur.execute('SELECT DISTINCT "_problem_id" FROM "StudentSubmissions"')
                problem_ids = [row[0] for row in cur.fetchall()]
                
                
                logging.info(f"Found {len(problem_ids)} problems in database")
                
                for problem_id in problem_ids:
                    # Lấy submissions cho từng problem
                    cur.execute(
                        'SELECT "_student_id", "_submission_id", "_code" '
                        'FROM "StudentSubmissions" WHERE "_problem_id"=%s',
                        (problem_id,)
                    )
                    rows = cur.fetchall()
                    
                    student_ids = set()
                    
                    for student_id, submission_id, code in rows:
                        # Tạo thư mục cho student
                        user_folder = os.path.join(base_dir, problem_id, student_id)
                        os.makedirs(user_folder, exist_ok=True)
                        
                        # Lưu file code
                        file_path = os.path.join(user_folder, f"{submission_id}.py")
                        
                        # Luôn ghi đè để cập nhật code mới nhất
                        with open(file_path, "w", encoding="utf-8") as f:
                            f.write(code if code else "# Empty submission")
                        
                        student_ids.add(student_id)
                    
                    submissions[problem_id] = list(student_ids)
                    logging.info(f"Fetched {len(rows)} submissions for problem {problem_id} from {len(student_ids)} students")
    
    except Exception as e:
        logging.error(f"Error fetching submissions from database: {e}", exc_info=True)
        raise
    
    return submissions


def scan_problem(problem_path: str) -> Problem:
    """Quét folder bài, gom file code theo user"""
    if not os.path.isdir(problem_path):
        raise ValueError(f"Problem path does not exist: {problem_path}")
    
    user_dirs = [
        os.path.join(problem_path, user)
        for user in os.listdir(problem_path)
        if os.path.isdir(os.path.join(problem_path, user))
    ]

    user_submissions = []
    for user_path in user_dirs:
        user = os.path.basename(user_path)
        py_files = []
        for root, _, files in os.walk(user_path):
            for f in files:
                if f.endswith(".py"):
                    py_files.append(os.path.join(root, f))
        if py_files:
            user_submissions.append(UserSubmission(user_id=user, files=py_files))

    problem_id = os.path.basename(problem_path)
    return Problem(problem_id=problem_id, user_submissions=user_submissions)


def run_copydetect(
    problem: Problem, 
    report_dir: str, 
    noise_t=25, 
    guarantee_t=30, 
    display_t=0.33,
    min_token_overlap=MIN_TOKEN_OVERLAP,
    min_similarity_percent=MIN_SIMILARITY_PERCENT
) -> Report:
    """
    Chạy CopyDetector giữa các user khác nhau và tạo báo cáo JSON.
    Chỉ lưu các trường hợp có token_overlap > min_token_overlap HOẶC similarity > min_similarity_percent
    """
    
    # Lấy danh sách thư mục user
    user_dirs = []
    for user in problem.user_submissions:
        if user.files:
            user_dir = os.path.dirname(user.files[0])
            user_dirs.append(user_dir)
    
    # Loại bỏ duplicates
    user_dirs = list(set(user_dirs))

    if len(user_dirs) < 2:
        raise ValueError(f"Problem {problem.problem_id} cần ít nhất 2 user để so sánh.")

    logging.info(f"Running CopyDetector for problem {problem.problem_id}")
    logging.info(f"User dirs: {user_dirs}")
    
    detector = CopyDetector(
        test_dirs=user_dirs,   
        ref_dirs=user_dirs,     
        noise_t=noise_t,
        guarantee_t=guarantee_t,
        display_t=display_t,
        silent=True
    )
    
    detector.run()
    
    # Lấy danh sách các cặp file đạo code
    copied_code_list = detector.get_copied_code_list()
    
    logging.info(f"Found {len(copied_code_list)} potential plagiarism cases")
    
    # Lọc và chuyển đổi sang PlagiarismCase
    cases = []
    filtered_count = 0
    
    for case in copied_code_list:
        test_sim, ref_sim, test_file, ref_file, hl_test, hl_ref, token_overlap = case
        
        # Lọc theo điều kiện
        max_similarity = max(test_sim, ref_sim) * 100
        
        if token_overlap > min_token_overlap or max_similarity > min_similarity_percent:
            filtered_count += 1
            
            # Đọc code gốc từ file
            try:
                with open(test_file, 'r', encoding='utf-8') as f:
                    test_code = f.read()
            except Exception as e:
                logging.warning(f"Cannot read {test_file}: {e}")
                test_code = "[Không thể đọc file]"
            
            try:
                with open(ref_file, 'r', encoding='utf-8') as f:
                    ref_code = f.read()
            except Exception as e:
                logging.warning(f"Cannot read {ref_file}: {e}")
                ref_code = "[Không thể đọc file]"
            
            plagiarism_case = PlagiarismCase(
                case_id=filtered_count,
                file1_path=test_file,
                file1_similarity=round(test_sim * 100, 2),
                file1_code=test_code,
                file1_highlighted=hl_test,
                file2_path=ref_file,
                file2_similarity=round(ref_sim * 100, 2),
                file2_code=ref_code,
                file2_highlighted=hl_ref,
                token_overlap=int(token_overlap),
                max_similarity=round(max_similarity, 2)
            )
            
            cases.append(plagiarism_case)
            
            logging.info(
                f"Case {filtered_count}: {test_file} <-> {ref_file} "
                f"(similarity: {max_similarity:.2f}%, tokens: {token_overlap})"
            )
    
    # Tạo file JSON
    os.makedirs(report_dir, exist_ok=True)
    json_file = os.path.join(report_dir, f"{problem.problem_id}_report.json")
    
    # Chuyển đổi sang dict để lưu JSON
    report_data = {
        "problem_id": problem.problem_id,
        "filter_criteria": {
            "min_token_overlap": min_token_overlap,
            "min_similarity_percent": min_similarity_percent
        },
        "total_cases_found": len(copied_code_list),
        "total_cases_filtered": filtered_count,
        "cases": [
            {
                "case_id": case.case_id,
                "file1": {
                    "path": case.file1_path,
                    "similarity_percent": case.file1_similarity,
                    "full_code": case.file1_code,
                    "highlighted_code": case.file1_highlighted
                },
                "file2": {
                    "path": case.file2_path,
                    "similarity_percent": case.file2_similarity,
                    "full_code": case.file2_code,
                    "highlighted_code": case.file2_highlighted
                },
                "token_overlap": case.token_overlap,
                "max_similarity_percent": case.max_similarity
            }
            for case in cases
        ]
    }
    
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(report_data, f, ensure_ascii=False, indent=2)
    
    logging.info(f"Report saved to {json_file}")
    
    return Report(
        problem_id=problem.problem_id,
        output_file=json_file,
        total_cases_found=len(copied_code_list),
        total_cases_filtered=filtered_count,
        filter_criteria={
            "min_token_overlap": min_token_overlap,
            "min_similarity_percent": min_similarity_percent
        },
        cases=cases
    )