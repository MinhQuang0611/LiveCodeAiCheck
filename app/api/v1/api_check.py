# api.py
import os
import logging
from fastapi import FastAPI, HTTPException, APIRouter, Query
from app.services.srv_check import (
    scan_problem, 
    run_copydetect, 
    fetch_submissions_from_db
)
from app.schemas.sche_check import Report

# Allow overriding directories via environment variables
DEFAULT_SUBMISSIONS_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../data/submissions")
)
DEFAULT_REPORTS_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../data/reports")
)

BASE_DIR = os.path.abspath(os.getenv("SUBMISSIONS_DIR", DEFAULT_SUBMISSIONS_DIR))
REPORT_DIR = os.path.abspath(os.getenv("REPORTS_DIR", DEFAULT_REPORTS_DIR))

os.makedirs(BASE_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)

router = APIRouter()


@router.get("/check_all")
async def check_all_problems(
    refresh_data: bool = Query(True, description="Fetch fresh data from database before checking")
):
    """
    Duyệt tất cả bài trong submissions và tạo report đạo code dạng JSON.
    
    Parameters:
    - refresh_data: True = fetch data mới từ DB trước khi check, False = dùng data có sẵn
    
    Chỉ lưu các trường hợp có token_overlap > 80 HOẶC similarity > 60%
    """
    summary = []
    logging.info(f"Using SUBMISSIONS_DIR={BASE_DIR}")
    logging.info(f"Using REPORTS_DIR={REPORT_DIR}")
    
    # Fetch data from database if requested
    if refresh_data:
        try:
            logging.info(f"Using SUBMISSIONS_DIR={BASE_DIR}")
            submissions = fetch_submissions_from_db(BASE_DIR)
            logging.info(f"Fetched data for {len(submissions)} problems")
        except Exception as e:
            logging.error(f"Error fetching data from database: {e}", exc_info=True)
            raise HTTPException(
                status_code=500,
                detail=f"Failed to fetch data from database: {str(e)}"
            )
    
    if not os.path.isdir(BASE_DIR):
        raise HTTPException(
            status_code=400, 
            detail=f"Submissions directory does not exist: {BASE_DIR}"
        )
    
    try:
        problem_dirs = os.listdir(BASE_DIR)
        logging.info(f"Found {len(problem_dirs)} problem directories")
    except Exception as e:
        logging.warning(f"Unable to list submissions dir {BASE_DIR}: {e}")
        raise HTTPException(status_code=500, detail=f"Cannot access submissions directory: {str(e)}")

    processed_count = 0
    skipped_count = 0
    error_count = 0
    
    for problem_id in problem_dirs:
        problem_path = os.path.join(BASE_DIR, problem_id)
        if not os.path.isdir(problem_path):
            continue

        try:
            problem = scan_problem(problem_path)

            if len(problem.user_submissions) < 2:
                skipped_count += 1
                logging.info(f"Skipping {problem_id}: only {len(problem.user_submissions)} submissions")
                continue

            report: Report = run_copydetect(problem, REPORT_DIR)
            processed_count += 1
            
            summary.append({
                "problem_id": report.problem_id,
                "total_cases_found": report.total_cases_found,
                "total_cases_filtered": report.total_cases_filtered,
                "filter_criteria": report.filter_criteria,
                "report_file": report.output_file,
                "num_plagiarism_cases": len(report.cases)
            })
            
            logging.info(
                f"Processed {problem_id}: "
                f"found {report.total_cases_found} cases, "
                f"filtered to {report.total_cases_filtered} cases"
            )

        except Exception as e:
            error_count += 1
            logging.error(f"Error processing {problem_id}: {e}", exc_info=True)
            summary.append({
                "problem_id": problem_id,
                "error": str(e),
                "status": "failed"
            })

    return {
        "total_problems_processed": processed_count,
        "total_problems_skipped": skipped_count,
        "total_problems_failed": error_count,
        "data_refreshed": refresh_data,
        "reports": summary
    }


@router.get("/check_problem/{problem_id}")
async def check_single_problem(
    problem_id: str,
    refresh_data: bool = Query(True, description="Fetch fresh data from database before checking")
):
    """
    Kiểm tra đạo code cho một bài cụ thể.
    
    Parameters:
    - problem_id: ID của bài cần check
    - refresh_data: True = fetch data mới từ DB trước khi check, False = dùng data có sẵn
    """
    
    # Fetch data from database if requested
    if refresh_data:
        try:
            logging.info(f"Fetching fresh data from database for problem {problem_id}...")
            submissions = fetch_submissions_from_db(BASE_DIR)
            
            if problem_id not in submissions:
                raise HTTPException(
                    status_code=404,
                    detail=f"Problem {problem_id} not found in database"
                )
            
            logging.info(f"Fetched data for problem {problem_id}")
        except HTTPException:
            raise
        except Exception as e:
            logging.error(f"Error fetching data from database: {e}", exc_info=True)
            raise HTTPException(
                status_code=500,
                detail=f"Failed to fetch data from database: {str(e)}"
            )
    
    problem_path = os.path.join(BASE_DIR, problem_id)
    
    if not os.path.isdir(problem_path):
        raise HTTPException(
            status_code=404, 
            detail=f"Problem {problem_id} not found in submissions directory"
        )
    
    try:
        problem = scan_problem(problem_path)
        
        if len(problem.user_submissions) < 2:
            return {
                "problem_id": problem_id,
                "message": f"Chỉ có {len(problem.user_submissions)} submission(s), cần ít nhất 2 để so sánh",
                "data_refreshed": refresh_data,
                "report": None
            }
        
        report: Report = run_copydetect(problem, REPORT_DIR)
        
        return {
            "problem_id": report.problem_id,
            "total_cases_found": report.total_cases_found,
            "total_cases_filtered": report.total_cases_filtered,
            "filter_criteria": report.filter_criteria,
            "report_file": report.output_file,
            "data_refreshed": refresh_data,
            "cases": [
                {
                    "case_id": case.case_id,
                    "file1_path": case.file1_path,
                    "file1_similarity": case.file1_similarity,
                    "file2_path": case.file2_path,
                    "file2_similarity": case.file2_similarity,
                    "token_overlap": case.token_overlap,
                    "max_similarity": case.max_similarity
                }
                for case in report.cases
            ]
        }
        
    except Exception as e:
        logging.error(f"Error checking {problem_id}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/refresh_data")
async def refresh_submissions_data():
    """
    Endpoint riêng để fetch data mới từ database mà không check đạo văn.
    Hữu ích khi chỉ muốn cập nhật data.
    """
    try:
        logging.info("Refreshing submissions data from database...")
        submissions = fetch_submissions_from_db(BASE_DIR)
        
        total_submissions = sum(len(students) for students in submissions.values())
        
        return {
            "status": "success",
            "total_problems": len(submissions),
            "total_students": total_submissions,
            "problems": {
                problem_id: len(students) 
                for problem_id, students in submissions.items()
            }
        }
    except Exception as e:
        logging.error(f"Error refreshing data: {e}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Failed to refresh data: {str(e)}"
        )