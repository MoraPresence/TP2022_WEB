from django.db import models

QUESTIONS = [
    {
        'id': question_id,
        'title': f'Do you see it too? Question #{question_id}',
        'text': f'Do you see it too? The red one runs all over the house! I can\'t catch her!!! Text of question #{question_id}',
        'answers_number': question_id * question_id,
        'tags': ['home' for i in range(question_id)]
    } for question_id in range(4)
]

ANSWERS = [
    {
        'id': answer_id,
        'title': f'Question #{answer_id}',
        'text': f'Text of question #{answer_id}',
        'answers_number': answer_id * answer_id,
        'tags': ['tag' for i in range(answer_id)]
    } for answer_id in range(2)
]
