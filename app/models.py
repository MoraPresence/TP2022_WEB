from django.db import models
from django.contrib.auth.models import User

QUESTIONS = [
    {
        'id': question_id,
        'title': f'Do you see it too? Question #{question_id}',
        'text': f'Do you see it too? The red one runs all over the house! I can\'t catch her!!! Text of question #{question_id}',
        'answers_number': question_id * question_id,
        'tags': ['home' for i in range(question_id)]
    } for question_id in range(10)
]

ANSWERS = [
    {
        'id': answer_id,
        'title': f'Answer #{answer_id}',
        'text': f'Text of answer #{answer_id}',
    } for answer_id in range(10)
]

PAGES = [
    {
        'page': QUESTIONS
    } for page_num in range(4)
]


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads')

    def __str__(self):
        return f'Profile Name {self.user.username}'


class Like(models.Model):
    count = models.IntegerField(default=0)


class Tag(models.Model):
    name = models.CharField(max_length=10)


class Question(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    answer_number = models.IntegerField()

    like = models.OneToOneField(
        Like,
        on_delete=models.CASCADE,
        primary_key=True)
    tag = models.ManyToManyField(Tag)
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'Question Author {self.author.user.username}'


class Answer(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    author = models.ManyToManyField(Profile)
    is_correct = models.BooleanField(default=False)
    like = models.OneToOneField(
        Like,
        on_delete=models.CASCADE,
        primary_key=True)
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE)

    def __str__(self):
        return f'Answer Author {self.author.user.username}'
