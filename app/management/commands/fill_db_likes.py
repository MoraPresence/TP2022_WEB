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
        author_list = User.objects.all()
        questions_list = Question.objects.all()
        answers_list = Answer.objects.all()
        votes = [1, -1]

        for i in range(total):
            user = random.choice(author_list)
            question = random.choice(questions_list)
            answer = random.choice(answers_list)

            like_q = Like.objects.create(target=question, user=user.profile, pk=question.id, vote_type=random.choice(votes))
            like_c = Like.objects.create(target=answer, user=user.profile, pk=answer.id, vote_type=random.choice(votes))
