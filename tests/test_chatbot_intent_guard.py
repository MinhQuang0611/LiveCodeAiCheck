from app.utils.chatbot_intent_guard import is_false_off_topic_for_current_context


def test_contextual_exercise_question_is_not_treated_as_off_topic():
    assert is_false_off_topic_for_current_context(
        intent="OFF_TOPIC",
        is_safe=True,
        question="Tính tổng hai số nguyên.",
        answer="a = int(input())\nb = int(input())\nprint(a + b)",
        user_question="Bài này làm như thế nào?",
    )


def test_unaccented_contextual_exercise_question_is_not_treated_as_off_topic():
    assert is_false_off_topic_for_current_context(
        intent="OFF_TOPIC",
        is_safe=True,
        question="Tính tổng hai số nguyên.",
        answer="a = int(input())\nb = int(input())\nprint(a + b)",
        user_question="bai nay lam nhu the nao?",
    )


def test_unrelated_question_stays_off_topic():
    assert not is_false_off_topic_for_current_context(
        intent="OFF_TOPIC",
        is_safe=True,
        question="Tính tổng hai số nguyên.",
        answer="a = int(input())\nb = int(input())\nprint(a + b)",
        user_question="Tình hình chính trị hôm nay thế nào?",
    )


def test_unsafe_question_stays_blocked():
    assert not is_false_off_topic_for_current_context(
        intent="OFF_TOPIC",
        is_safe=False,
        question="Tính tổng hai số nguyên.",
        answer="a = int(input())\nb = int(input())\nprint(a + b)",
        user_question="Bài này làm như thế nào?",
    )
