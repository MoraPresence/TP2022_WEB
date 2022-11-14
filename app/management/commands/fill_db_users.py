from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from app.models import Profile

from faker import Faker

import requests

fake = Faker()


class Command(BaseCommand):
    help = u'Заполнение базы данных случайными пользователями'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help=u'Количество создаваемых пользователей')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            Profile.user = User.objects.create_user(
                username=fake.name(),
                email=fake.email(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                password='1111')

            url = fake.image_url()
            s = requests.get(url)

            image_name = fake.word()

            with open(f"uploads/{image_name}.png", "wb") as f:
                f.write(s.content)

            Profile.image = f"uploads/{image_name}.png"
