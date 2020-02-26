import json
import pytest
import System
import Professor
import TA
import Student
import User
import string

#Defining variables for testing use.
user = 'goggins'
password = 'augurrox'
student = 'hdjsr7'
course = 'cloud_computing'
assignment = 'assignment1'

#Function that creates random strings for password testing
def randomString(stringLenth = 10):
	letters = string.ascii_lowercase
	return ''.join(random.choice(letters) for i in range(stringLenth))

#Tests login is user is of the role 'professor'
def test_login(grading_system):
	users = grading_system.users
	grading_system.login(user, password)
	if users[user]['role'] == 'Professor':
		assert True

#Checks password matching
def test_password(grading_system):
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
		if users[student]['courses'][course][assignment]['grade']:
			assert False
		else:
			assert True


def test_addStudent(grading_system):
	users = grading_system.users
	courses = grading_system.courses
	professor = Professor.Professor(user, users, courses)
	professor.add_student('hdjsr7', 'cloud_computing')

	for key in users:
		if key == 'hdjsr7':
			assert True
		else:
			assert False

def test_dropStudent(grading_system):
	users = grading_system.users
	courses = grading_system.courses
	professor = Professor.Professor(user, users, courses)
	professor.drop_student(student, 'comp_sci')

	if 'comp_sci' in users[student]['courses']:
			assert True
	else:
			assert False 




	




	





@pytest.fixture
def grading_system():
	gradingSystem = System.System()
	gradingSystem.load_data()
	return gradingSystem