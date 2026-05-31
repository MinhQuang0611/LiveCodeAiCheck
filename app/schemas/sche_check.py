# schemas/sche_check.py
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class UserSubmission:
    user_id: str
    files: List[str]  

@dataclass
class Problem:
    problem_id: str
    user_submissions: List[UserSubmission]

@dataclass
class PlagiarismCase:
    case_id: int
    file1_path: str
    file1_similarity: float
    file1_code: str
    file1_highlighted: str
    file2_path: str
    file2_similarity: float
    file2_code: str
    file2_highlighted: str
    token_overlap: int
    max_similarity: float

@dataclass
class Report:
    problem_id: str
    output_file: str
    total_cases_found: int
    total_cases_filtered: int
    filter_criteria: dict
    cases: List[PlagiarismCase]