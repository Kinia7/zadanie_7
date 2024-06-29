from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
import random
from datetime import date

fake = Faker()

engine = create_engine('postgresql://user:password@localhost/mydatabase')
Session = sessionmaker(bind=engine)
session = Session()

# Tworzenie przykładowych danych
groups = [Group(name=f'Group {i}') for i in range(1, 4)]
lecturers = [Lecturer(fullname=fake.name()) for _ in range(4)]
courses = [Course(name=fake.word(), lecturer=random.choice(lecturers)) for _ in range(6)]
students = [Student(fullname=fake.name(), group=random.choice(groups)) for _ in range(30)]

session.add_all(groups + lecturers + courses + students)
session.commit()

for student in students:
    for course in courses:
        for _ in range(random.randint(1, 20)):
            grade = Grade(
                student=student,
                course=course,
                grade=round(random.uniform(2, 5), 2),
                date_received=fake.date_between(start_date='-2y', end_date='today')
            )
            session.add(grade)

session.commit()
