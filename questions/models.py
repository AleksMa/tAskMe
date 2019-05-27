from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation


# TODO: problems
# 1   Done
# 2   Done
# 3   Done
# 4   Done
# 5
# 6   Done
# 7   Done

class Tag(models.Model):
    text = models.CharField(max_length=64, unique=True, blank=False)

    def __str__(self):
        return self.text


class QuestionManager(models.Manager):
    def order_by_date(self, amount):
        return self.order_by('-created_date')[:amount]

    def order_by_hot(self):
        return self.order_by('-rate')

    def filter_by_tag(self, tag):
        try:
            return super().filter(tags__text=tag.text)
        except(ObjectDoesNotExist):
            return self.none()


class Profile(AbstractUser):
    photo = models.TextField(default='images/Danil.jpg')

    def __str__(self):
        return self.first_name


class Like(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    positive = models.IntegerField(default=0)
    negative = models.IntegerField(default=0)



class Answer(models.Model):
    title = models.CharField(max_length=140, default="Title", blank=False)
    content = models.TextField(default="")
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    isRight = models.BooleanField(default=False)
    rate = models.IntegerField(default=0)

    like = GenericRelation(Like)

    def __str__(self):
        return self.content


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=140, default="Title", blank=False)
    content = models.TextField(default="")
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    answers = models.ManyToManyField(Answer)
    created_date = models.DateTimeField(default=timezone.now)
    tags = models.ManyToManyField(Tag)
    rate = models.IntegerField(default=0)

    list = QuestionManager()
    like = GenericRelation(Like)

    def __str__(self):
        return self.title










'''
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation


# TODO: problems
# 1   Done
# 2   Done
# 3   Done
# 4   Done
# 5
# 6   Done
# 7   Done

class Tag(models.Model):
    text = models.CharField(max_length=64, unique=True, blank=False)

    def __str__(self):
        return self.text


class QuestionManager(models.Manager):
    def order_by_date(self, amount):
        return self.order_by('-created_date')[:amount]

    def order_by_hot(self):
        return self.order_by('-rate')

    def filter_by_tag(self, tag):
        try:
            return super().filter(tags__text=tag.text)
        except(ObjectDoesNotExist):
            return self.none()


class Profile(AbstractUser):
    photo = models.TextField(default='images/Danil.jpg')

    def __str__(self):
        return self.first_name


class Like(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    positive = models.IntegerField(default=0)
    negative = models.IntegerField(default=0)


class Post(models.Model):
    title = models.CharField(max_length=140, default="Title", blank=False)
    content = models.TextField(default="")
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    rate = models.IntegerField(default=0)
    like = GenericRelation(Like)

    class Meta:
        abstract = True


class Answer(Post):
    isRight = models.BooleanField(default=False)

    def __str__(self):
        return self.content


class Question(Post):
    objects = QuestionManager()
    answers = models.ManyToManyField(Answer)
    tags = models.ManyToManyField(Tag)
    list = QuestionManager()

    def __str__(self):
        return self.title


'''
