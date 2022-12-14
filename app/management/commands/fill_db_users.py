import os, random

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from app.models import Profile

from faker import Faker

import requests

fake = Faker()


# TODO: BALCO

class Command(BaseCommand):
    help = u'Заполнение базы данных случайными пользователями'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help=u'Количество создаваемых пользователей')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            user = User.objects.create_user(
                username=fake.first_name() + str(random.randint(1, 10000)) + fake.last_name(),
                email=fake.email(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                password='1111')

            image = random.choice(os.listdir("uploads/"))
            profile = Profile.objects.create(user=user)

            # url = fake.image_url()
            # s = requests.get(url)
            #
            # image_name = fake.word()
            #
            # with open(f"uploads/{image_name}.png", "wb") as f:
            #     f.write(s.content)
            #
            # image = f"uploads/{image_name}.png"
            # profile = Profile.objects.create(user=user, image=image)
