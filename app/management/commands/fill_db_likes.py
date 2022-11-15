from django.core.management.base import BaseCommand

import random
from faker import Faker

fake = Faker()

from app.models import *


class Command(BaseCommand):
    help = u'Заполнение базы данных случайными данными'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help=u'Множитель заполнения')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        author_list = Profile.objects.all()
        questions_list = Question.objects.all()
        answers_list = Answer.objects.all()

        for i in range(total):
            user = random.choice(author_list)
            question = random.choice(questions_list)
            answer = random.choice(answers_list)

            like_question = Like.objects.create(content_type=ContentType.objects.get_for_model(question),
                                                object_id=question.id, user=user,
                                                count=random.randint(0, 100))
            like_answer = Like.objects.create(content_type=ContentType.objects.get_for_model(answer),
                                              object_id=answer.id,
                                              user=user,
                                              count=random.randint(0, 100))
