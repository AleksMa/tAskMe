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


def get_random_element(qs, min_pk, max_pk):

    if max_pk is None:
        max_pk = qs.aggregate(Max('pk'))['pk__max']
    if min_pk is None:
        min_pk = qs.aggregate(Min('pk'))['pk__min']
    while True:

        try_pk = random.randint(min_pk, max_pk)
        try:
            found = qs.get(pk=try_pk)
            return found
        except qs.model.DoesNotExist:
            pass


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

        if questions_cnt is not None:
            self.generate_questions(questions_cnt)

        if answers_cnt is not None:
            self.generate_answers(answers_cnt)

        if tags_cnt is not None:
            self.generate_tags(tags_cnt)

    def generate_users(self, users_cnt):
        print(f"GENERATE USERS {users_cnt}")
        for i in range(users_cnt):
            name = choice(list(unames))
            p = Profile.objects.create(first_name=name,
                                       last_name=name,
                                       username=name+str(fake.random_int(1, 1024)),
                                       password='123456',
                                       photo=choice(list(paths)))

    def generate_tags(self, tags_cnt):
        print(f"GENERATE TAGS {tags_cnt}")
        for i in range(tags_cnt):
            t = Tag(text=fake.word())
            t.save()

    def generate_questions(self, questions_cnt):
        print(f"GENERATE QUESTIONS {questions_cnt}")
        for i in range(questions_cnt):
            q = Question.objects.create(
                author=get_random_element(Profile.objects, None, None),
                title=fake.sentence(),
                content='\n'.join(fake.sentences(fake.random_int(1, 5))),
                rate=fake.random_int(1, 100))
            l = Like(question=q, positive=fake.random_int(1, 100), negative=-fake.random_int(1, 100))
            l.save()
            q.rate = l.positive + l.negative
            q.save()
            #for j in range(1, fake.random_int(1, 7)):
            #    q.tags.add(choice(tags))

    def generate_answers(self, answers_cnt):
        print(f"GENERATE ANSWERS {answers_cnt}")
        for i in range(answers_cnt):
            a = Answer.objects.create(
                author=get_random_element(Profile.objects, None, None),
                question=get_random_element(Question.objects, None, None),
                content=fake.sentence())
            l = Like(answer=a, positive=fake.random_int(1, 100), negative=-fake.random_int(1, 100))
            l.save()
            a.rate = l.positive + l.negative
            a.save()
