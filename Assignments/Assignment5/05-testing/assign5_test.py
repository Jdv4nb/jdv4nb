import json
import pytest
import System
import Professor
import TA
import Student
import string
import random

#Defining variables for testing use.
user = 'goggins'
password = 'augurrox'
student = 'hdjsr7'
course = 'cloud_computing'
assignment = 'assignment1'
score = 43


#Function that creates random strings for password testing


#Tests login is user is of the role 'professor'
def test_login(grading_system):
    users = grading_system.users
    grading_system.login(user, password)
    if users[user]['role'] == 'professor':
        assert True

#Checks password matching
def test_password(grading_system):
    letters = string.ascii_lowercase
    stringLength = 10
    randomString = ''.join(random.choice(letters) for i in range(stringLength))
    users = grading_system.users
    grading_system.check_password(user, randomString)
    if randomString == users[user]['password']:
        if grading_system.check_password(user,password):
            assert True

def test_gradeChange(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    professor = Professor.Professor(user,users,courses)
    professor.change_grade(student, course, assignment, 50)

    for key in users:
        if users[student]['courses'][course][assignment]['grade'] == 0:
            assert False
        else:
            assert True


def test_addStudent(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    professor = Professor.Professor(user, users, courses)
    professor.add_student('hdjsr', 'cloud_computing')

    for key in users:
        if key == 'hdjsr':
            assert True
        else:
            assert False

def test_dropStudent(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    professor = Professor.Professor(user, users, courses)
    professor.drop_student(student, 'databases')

    if 'databases' in users[student]['courses']:
        assert False
    else:
        assert True

def test_submitAssign(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    student = Student.Student(student, users, courses)
    student.submit_assignment('software_engineering', 'assignment1', 'Blah Blah Blah', '1/1/20')

    for key in users:
        if '1/1/20' in users ['hdjsr7']['courses']['software_engineering']['assignment1']['submission_date']:
            assert True
        else:
            assert False

def test_onTime(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    stdnt = Student.Student(student, users, courses)

    if stdnt.check_ontime('1/5/20', '1/4/20'):
        assert False
    else:
        assert True

def test_gradeCheck(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    gradeTest = Student.Student(student, users, courses)
    grades = gradeTest.check_grades(course)

    if grades[0][1] == 43:
        assert True
    else:
        assert False 
    
def test_createAssign(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    professor = Professor.Professor(user, users, courses)
    professor.create_assignment('assignment3', '2/22/2020', 'cloud_computing')

    assignments = []
    for key in courses:
        assignments.append([key, courses[key]])

    if assignments[1][1]['assignments']['assignment3']:
        assert True
    else:
        assert False




    




    





@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem