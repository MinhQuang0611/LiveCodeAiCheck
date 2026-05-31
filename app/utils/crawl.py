import os
import psycopg
from copydetect import CopyDetector
from schemas import UserSubmission, Problem, Report
from service import run_copydetect
from settings import settings

BASE_DIR = os.path.join(os.path.dirname(__file__), "../../data/submissions")
BASE_DIR = os.path.abspath(BASE_DIR)

REPORT_DIR = os.path.join(os.path.dirname(__file__), "../../data/reports")
REPORT_DIR = os.path.abspath(REPORT_DIR)

os.makedirs(BASE_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)

def fetch_submissions():
    """Lấy dữ liệu StudentSubmissions từ PostgreSQL"""
    submissions = {}

    with psycopg.connect(settings.DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT DISTINCT "_problem_id" FROM "StudentSubmissions"')
            problem_ids = [row[0] for row in cur.fetchall()]

            for problem_id in problem_ids:
                cur.execute('SELECT "_student_id", "_submission_id", "_code" FROM "StudentSubmissions" WHERE "_problem_id"=%s', (problem_id,))
                rows = cur.fetchall()
                for student_id, submission_id, code in rows:
                    user_folder = os.path.join(BASE_DIR, problem_id, student_id)
                    os.makedirs(user_folder, exist_ok=True)

                    file_path = os.path.join(user_folder, f"{submission_id}.py")
                    if not os.path.exists(file_path):
                        with open(file_path, "w", encoding="utf-8") as f:
                            f.write(code)
                
                submissions[problem_id] = list(set([row[0] for row in rows]))

    return submissions

def run_auto_check():
    """Tự động cào data + check đạo code"""
    os.makedirs(REPORT_DIR, exist_ok=True)
    submissions = fetch_submissions()
    summary = []

    for problem_id, user_ids in submissions.items():
        problem_path = os.path.join(BASE_DIR, problem_id)

        user_dirs = [
            os.path.join(problem_path, user_id)
            for user_id in user_ids
            if os.path.isdir(os.path.join(problem_path, user_id))
        ]

        if len(user_dirs) < 2:
            print(f"Bỏ qua {problem_id}: chỉ có {len(user_dirs)} người nộp.")
            continue

        print(f"\n Kiểm tra đạo code bài {problem_id}...")

        user_to_files = {}
        for user_path in user_dirs:
            user = os.path.basename(user_path)
            py_files = [os.path.join(user_path, f) for f in os.listdir(user_path) if f.endswith(".py")]
            if py_files:
                user_to_files[user] = py_files

        test_files, ref_files = [], []
        users = list(user_to_files.keys())
        for i in range(len(users)):
            for j in range(len(users)):
                if i != j:
                    test_files.extend(user_to_files[users[i]])
                    ref_files.extend(user_to_files[users[j]])

        if not test_files or not ref_files:
            print(f" Bỏ qua {problem_id}: không có file .py hợp lệ.")
            continue

        report = run_copydetect(
            Problem(problem_id=problem_id, user_submissions=[UserSubmission(user, files) for user, files in user_to_files.items()]),
            REPORT_DIR
        )
        summary.append(report)
        print(f" Báo cáo đã tạo: {report.output_file}")

    print("\n====================== TỔNG KẾT ======================")
    for r in summary:
        print(f" Bài {r.problem_id}: {r.num_files} file → báo cáo: {r.output_file}")
    print("======================================================")

if __name__ == "__main__":
    run_auto_check()
