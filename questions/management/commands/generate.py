import random
from django.db import transaction
from django.core.management.base import BaseCommand
from questions.models import Question, Profile, Tag, Answer, Like
from django.db.models import Max, Min
from faker import Faker
from random import choice

fake = Faker()
paths = ['images/Anton.jpg', 'images/Danil.jpg', 'images/MiSa.jpg']
tags = ['linear-algebra', 'matrices', 'permutations', 'combinatorics', 'calculus', 'real-analysis', 'integration']
unames = ['Anton', 'MiSa', 'Danil', 'Vlad', 'Ann', 'Sawa', 'Dinar']


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--questions', type=int)
        parser.add_argument('--users', type=int)
        parser.add_argument('--tags', type=int)
        parser.add_argument('--answers', type=int)

    # @transaction.atomic()
    def handle(self, *args, **options):
        users_cnt = options['users']
        questions_cnt = options['questions']
        answers_cnt = options['answers']
        tags_cnt = options['tags']

        if users_cnt is not None:
            self.generate_users(users_cnt)

        if answers_cnt is not None:
            self.generate_answers(answers_cnt)

        if tags_cnt is not None:
            self.generate_tags(tags_cnt)

        if questions_cnt is not None:
            self.generate_questions(questions_cnt)

    def generate_users(self, users_cnt):
        print(f"GENERATE USERS {users_cnt}")
        for i in range(users_cnt):
            name = choice(unames)
            p = Profile.objects.create(first_name=name,
                                       last_name=name,
                                       username=name + str(fake.random_int(1, 1024)),
                                       password='123456',
                                       photo=choice(paths))

    def generate_tags(self, tags_cnt):
        print(f"GENERATE TAGS {tags_cnt}")
        for i in range(tags_cnt):
            t = Tag(text=fake.word())
            t.save()

    def generate_questions(self, questions_cnt):
        print(f"GENERATE QUESTIONS {questions_cnt}")
        ans = list(Answer.objects.all())
        ts  = list(Answer.objects.all())
        for i in range(questions_cnt):
            q = Question.objects.create(
                author=choice(Profile.objects.all()),
                title=fake.sentence(),
                content='\n'.join(fake.sentences(fake.random_int(1, 5))),
                rate=fake.random_int(1, 100),
                id=Question.objects.all().count() + 1)
            l = Like(positive=fake.random_int(1, 100), negative=-fake.random_int(1, 100))
            l.content_object = q
            l.save()
            q.rate = l.positive + l.negative
            q.save()
            for j in range(1, fake.random_int(2, 5)):
                q.answers.add(choice(ans))
            for j in range(1, fake.random_int(2, 5)):
                q.tags.add(choice(ts))

    def generate_answers(self, answers_cnt):
        print(f"GENERATE ANSWERS {answers_cnt}")
        ps = list(Profile.objects.all())
        for i in range(answers_cnt):
            a = Answer.objects.create(
                author=choice(ps),
                content=fake.sentence())
            l = Like(positive=fake.random_int(1, 100), negative=-fake.random_int(1, 100))
            l.content_object = a
            l.save()
            a.rate = l.positive + l.negative
            a.save()
