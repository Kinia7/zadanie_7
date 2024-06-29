from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    students = relationship('Student', back_populates='group')

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    fullname = Column(String, nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship('Group', back_populates='students')
    grades = relationship('Grade', back_populates='student')

class Lecturer(Base):
    __tablename__ = 'lecturers'
    id = Column(Integer, primary_key=True)
    fullname = Column(String, nullable=False)
    courses = relationship('Course', back_populates='lecturer')

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    lecturer_id = Column(Integer, ForeignKey('lecturers.id'))
    lecturer = relationship('Lecturer', back_populates='courses')
    grades = relationship('Grade', back_populates='course')

class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))
    grade = Column(Float, nullable=False)
    date_received = Column(Date, nullable=False)
    student = relationship('Student', back_populates='grades')
    course = relationship('Course', back_populates='grades')
