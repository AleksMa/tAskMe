from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class Tag(models.Model):
    text = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.text


class QuestionManager(models.Manager):
    def order_by_date(self, amount):
        return self.order_by('-created_date')[:amount]

    def order_by_hot(self):
        return self.order_by('-rate')

    def filter_by_tag(self, tag):
        try:
            return super().filter(tags__in=[Tag.objects.get(title=tag).id])
        except(ObjectDoesNotExist):
            return self.none()


class Profile(AbstractUser):
    photo = models.TextField(default='images/Danil.jpg')

    def __str__(self):
        return self.first_name


class Answer(models.Model):
    title = models.CharField(max_length=140, default="")
    content = models.TextField(default="")
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    isRight = models.BooleanField(default=False)
    rate = models.IntegerField(default=0)

    def __str__(self):
        return self.content


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=140, default="")
    content = models.TextField(default="")
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    answers = models.ManyToManyField(Answer)
    created_date = models.DateTimeField(default=timezone.now)
    tags = models.ManyToManyField(Tag)
    rate = models.IntegerField(default=0)
    list = QuestionManager()

    def __str__(self):
        return self.title


class Like(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, default=None)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True, default=None)
    positive = models.IntegerField(default=0)
    negative = models.IntegerField(default=0)
