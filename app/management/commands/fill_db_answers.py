from django.core.management.base import BaseCommand

import random
from faker import Faker

from app.models import *

fake = Faker()


class Command(BaseCommand):
    help = u'Заполнение базы данных случайными ответами'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help=u'Количество создаваемых ответов')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        author_list = Profile.objects.all()
        questions_list = Question.objects.all()

        for i in range(total):
            author = random.choice(author_list)
            question = random.choice(questions_list)
            answer = Answer.objects.create(text=fake.text(), question=question, author=author)
