from django.db import transaction
from django.core.management.base import BaseCommand
from questions.models import Question, Profile, Tag, Answer, Like
from faker import Faker
from random import choice

fake = Faker()
paths = ['images/Anton.jpg', 'images/Danil.jpg', 'images/MiSa.jpg']
tags = ['linear-algebra' 'matrices' 'permutations' 'combinatorics' 'calculus' 'real-analysis' 'integration']
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
            Tag.objects.create(text=fake.word())

    def generate_questions(self, questions_cnt):
        print(f"GENERATE QUESTIONS {questions_cnt}")
        uids = list(
            Profile.objects.values_list(
                'id', flat=True))
        tags = list(
            Tag.objects.values_list(
                'id', flat=True))
        for i in range(questions_cnt):
            q = Question.objects.create(
                author_id=choice(uids),
                title=fake.sentence(),
                text='\n'.join(fake.sentences(fake.random_int(2, 5))),
                rating=fake.random_int(1, 100))
            l = Like(content_object=q, positive=fake.random_int(1, 100), negative=-fake.random_int(1, 100))
            l.save()
            q.rate = l.positive + l.negative
            q.save()
            for j in range(1, fake.random_int(1, 7)):
                q.tag.add(choice(tags))

    def generate_answers(self, answers_cnt):
        print(f"GENERATE ANSWERS {answers_cnt}")
        uids = list(
            Profile.objects.values_list(
                'id', flat=True))
        qids = list(
            Question.objects.values_list(
                'id', flat=True))
        for i in range(answers_cnt):
            a = Answer.objects.create(
                author_id=choice(uids),
                question_id=choice(qids),
                text=fake.sentence(),
                rating=fake.random_int(1, 100))
            l = Like(content_object=a, positive=fake.random_int(1, 100), negative=-fake.random_int(1, 100))
            l.save()
            a.rating = l.positive + l.negative
            a.save();
