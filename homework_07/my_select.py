from sqlalchemy import func, desc
from models import Student, Grade, Course, Group, Lecturer
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('postgresql://user:password@localhost/mydatabase')
Session = sessionmaker(bind=engine)

def select_1():
    session = Session()
    result = session.query(
        Student.fullname, 
        func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).join(Grade).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
    session.close()
    return result

def select_2(course_id):
    session = Session()
    result = session.query(
        Student.fullname,
        func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).join(Grade).filter(Grade.course_id == course_id).group_by(Student.id).order_by(desc('avg_grade')).first()
    session.close()
    return result

def select_3(course_id):
    session = Session()
    result = session.query(
        Group.name,
        func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).join(Student).join(Grade).filter(Grade.course_id == course_id).group_by(Group.id).all()
    session.close()
    return result

def select_4():
    session = Session()
    result = session.query(
        Group.name,
        func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).join(Student).join(Grade).group_by(Group.id).all()
    session.close()
    return result

def select_5(lecturer_id):
    session = Session()
    result = session.query(
        Course.name
    ).filter(Course.lecturer_id == lecturer_id).all()
    session.close()
    return result

def select_6(group_id):
    session = Session()
    result = session.query(
        Student.fullname
    ).filter(Student.group_id == group_id).all()
    session.close()
    return result

def select_7(group_id, course_id):
    session = Session()
    result = session.query(
        Student.fullname,
        Grade.grade
    ).join(Grade).filter(Student.group_id == group_id, Grade.course_id == course_id).all()
    session.close()
    return result

def select_8(lecturer_id):
    session = Session()
    result = session.query(
        func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).join(Course).filter(Course.lecturer_id == lecturer_id).all()
    session.close()
    return result

def select_9(student_id):
    session = Session()
    result = session.query(
        Course.name
    ).join(Grade).filter(Grade.student_id == student_id).distinct().all()
    session.close()
    return result

def select_10(lecturer_id, student_id):
    session = Session()
    result = session.query(
        Course.name
    ).join(Grade).filter(Course.lecturer_id == lecturer_id, Grade.student_id == student_id).all()
    session.close()
    return result
