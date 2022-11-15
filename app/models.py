from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models import Count


class ProfileManager(models.Manager):
    use_for_related_fields = True

    def get_users(self):
        return self.get_queryset()


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE)
    image = models.ImageField()

    objects = ProfileManager()

    def __str__(self):
        return f'{self.user.username}'

    @property
    def get_avatar(self):
        if self.image:
            return self.image.url
        else:
            return settings.STATIC_URL + 'img/cat01.jpg'


class LikeManager(models.Manager):
    use_for_related_fields = True

    def like_sort(self):
        return self.get_queryset().order_by('-count')


class Like(models.Model):
    count = models.PositiveIntegerField(default=0)
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )
    object_id = models.IntegerField()

    objects = LikeManager()

    class Meta:
        ordering = ['-count']

    def __str__(self):
        return f'{self.count}'


class Tag(models.Model):
    name = models.CharField(max_length=10)

    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.name}'


class QuestionManager(models.Manager):
    def hot_questions(self):
        return self.get_queryset().order_by('-likes').annotate(answers_count=Count('answer'))

    def new_questions(self):
        return self.get_queryset().order_by('-creating_date').annotate(answers_count=Count('answer'))

    def tag_questions(self, tag):
        return self.get_queryset().filter(tag__name__contains=tag).annotate(answers_count=Count('answer'))

    def get_count_questions_by_tag(self, tag):
        return self.get_queryset().filter(tag__name__contains=tag).count()


class Question(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=300)

    tag = models.ManyToManyField(Tag)
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )

    likes = GenericRelation(Like, related_query_name='likes')

    creating_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    objects = QuestionManager()

    class Meta:
        ordering = ['-creating_date']

    def __str__(self):
        return f'Question Author {self.author.user.username}'


def get_best_members():
    answers_count = {}
    for profile in Profile.objects.all():
        answers_count[profile] = Answer.objects.get_count_answers_by_profile(profile.user.username)
    best_members = sorted(answers_count, key=answers_count.get, reverse=True)[0:5]

    return best_members


def get_popular_tags():
    question_count = {}
    for tag in Tag.objects.all():
        question_count[tag] = Question.objects.get_count_questions_by_tag(tag)
    popular_tags = sorted(question_count, key=question_count.get, reverse=True)[0:5]

    return popular_tags


class AnswerManager(models.Manager):
    use_for_related_fields = True

    def get_count_answers_by_profile(self, profile):
        return self.get_queryset().filter(author__user__username__contains=profile).count()


class Answer(models.Model):
    text = models.CharField(max_length=300)
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE)

    objects = AnswerManager()

    likes = GenericRelation(Like, related_query_name='likes')

    def __str__(self):
        return f'Answer Author {self.author.user.username}'
