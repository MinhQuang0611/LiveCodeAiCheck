import re
from typing import Optional


_CONTEXTUAL_EXERCISE_PATTERNS = [
    r"\bb[aà]i\s+(n[aà]y|n[àa]o|tr[êe]n)\b",
    r"\b[dđ][eề]\s+(n[aà]y|b[aà]i|tr[êe]n)\b",
    r"\bcode\s+(n[aà]y|tr[êe]n|c[uủ]a\s+em|c[uủ]a\s+t[oô]i)\b",
    r"\b(l[aà]m|gi[aả]i|x[ưử]\s*l[yý]|ti[ếe]p\s*c[aậ]n)\s+(nh[ưu]\s+th[ếe]\s+n[aà]o|sao|th[ếe]\s+n[aà]o)\b",
    r"\b(h[ưư]ớng\s*d[aẫ]n|g[ợo]i\s*[ýy]|gi[aả]i\s*th[ií]ch|ph[aâ]n\s*t[ií]ch)\b",
    r"\b(sai|l[ỗo]i|bug|debug|t[ốo]i\s*[ưu]u|thu[aậ]t\s*to[aá]n|logic)\b",
    r"\bbai\s+(nay|nao|tren)\b",
    r"\bde\s+(nay|bai|tren)\b",
    r"\b(lam|giai|xu\s*ly|tiep\s*can)\s+(nhu\s+the\s+nao|sao|the\s+nao|ntn)\b",
    r"\b(huong\s*dan|goi\s*y|giai\s*thich|phan\s*tich)\b",
    r"\b(loi|toi\s*uu|thuat\s*toan)\b",
]


def _has_exercise_context(question: Optional[str], answer: Optional[str], topic_name: Optional[str] = None) -> bool:
    return bool((question and question.strip()) or (answer and answer.strip()) or (topic_name and topic_name.strip()))


def _looks_like_contextual_exercise_question(user_question: str) -> bool:
    normalized = re.sub(r"\s+", " ", (user_question or "").strip().lower())
    if not normalized:
        return False
    return any(re.search(pattern, normalized) for pattern in _CONTEXTUAL_EXERCISE_PATTERNS)


def is_false_off_topic_for_current_context(
    *,
    intent: str,
    is_safe: bool,
    question: Optional[str],
    answer: Optional[str],
    user_question: str,
    topic_name: Optional[str] = None,
) -> bool:
    if intent != "OFF_TOPIC" or not is_safe:
        return False
    return _has_exercise_context(question, answer, topic_name) and _looks_like_contextual_exercise_question(user_question)
