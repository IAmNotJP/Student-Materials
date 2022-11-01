import pytest
import unittest
import System
import User
import Staff
import Student
import TA
import Professor

def test_login_System():
	
	gradeSystem.login("hdjsr7","pass1234")
	assert gradeSystem.usr.name =="hdjsr7"
	
	
def test_check_Password():
	pass1 = "pass1234"
	pass2 = "Pass1234"
	pass3 = "1ssap"
	
	assert gradeSystem.check_password("user1",pass1)==True
	assert gradeSystem.check_password("user1",pass2)==False
	assert gradeSystem.check_password("user1",pass3)==False
	
def test_change_Grade():
	gradeSystem.login("cmhbf5","bestTA")
	gradeSystem.usr.change_grade('hdjsr', 'software_engineering', 'assignment1', 50)
	assert gradeSystem.users['yted91']["courses"]["software_engineering"]["assignment1"]["grade"] == 100
	
def test_create_Assignment():
	gradeSystem.login("saab","boomr345")
	gradeSystem.usr.create_assignment("assignment 3","1/2/34","comp_sci")
	assert gradeSystem.courses["comp_sci"]["assignments"]["assignment 3"]["due_date"] == "4/3/21"
	
def test_add_Student():
	gradeSystem.login("saab","boomr345")	
	gradeSystem.usr.add_student("yted91", "comp_sci")	
	assert gradeSystem.users["yted91"]["courses"][2] != "comp_sci"
	
def test_drop_Student():
	gradeSystem.login("goggins","augurrox")
	gradeSystem.usr.drop_student("hdjsr7", "software_engineering")
	assert gradeSystem.users["hdjsr7"]["courses"][0] != "software_engineering"
	
def test_submit_Assignment():
	gradeSystem.login("yted91","imoutofpasswordnames")
	gradeSystem.usr.submit_assignment("comp_sci","assignment1","Oh boy im failing", "9/9/99")
	assert gradeSystem.users["yted91"]["courses"][2].length() == 1
	
def test_check_Grades():	
	gradeSystem.login("yted91","imoutofpasswordnames")
	grades = gradeSystem.usr.check_grades("cloud_computing")
	assert sum(grades) == 100
	
def test_check_Ontime():
	gradeSystem.login("yted91","imoutofpasswordnames")
	assert gradeSystem.usr.check_ontime("1/7/20", "1/10/20") == True
	assert gradeSystem.usr.check_ontime("2/7/20", "2/3/20") == False
	
def test_view_assignments():
	gradeSystem.login('hdjsr7', 'pass1234')
	assignments = gradeSystem.usr.view_assignments('databases')
	assert assignments[0] == "assignment1"
	
def test_duplicate_Add():
	gradeSystem.login("goggins","augurrox")
	assert gradeSystem.usr.add_student("yted91", "comp_sci")
	assert gradeSystem.users["yted91"]["courses"][2] != gradeSystem.users["yted91"]["courses"][3]
	
def test_drop_wrong_Class():
	gradeSystem.login("goggins","augurrox")
	gradeSystem.usr.drop_student("yted91", "databases")
	assert gradeSystem.users["hdjsr7"]["courses"][1] == "databases"
	
def test_submit_Duplicate():
	gradeSystem.login('hdjsr7', 'pass1234')
	gradeSystem.usr.submit_assignment("databases","assignment1","Im a dupe!", "1/1/25")
	assignments = gradeSystem.usr.view_assignments('databases')
	assert assignments[0].assignment_name!=assignments[2].assignment_name
	
def test_negative_Assignment():
	gradeSystem.login("cmhbf5","bestTA")
	gradeSystem.usr.change_grade('hdjsr', 'software_engineering', 'assignment1', -50)
	assert assert gradeSystem.users['yted91']["courses"]["software_engineering"]["assignment1"]["grade"] >= 0;
	
def test_negative_Assignment():
	gradeSystem.login("cmhbf5","bestTA")
	gradeSystem.usr.change_grade('hdjsr', 'software_engineering', 'assignment1', 150)
	assert assert gradeSystem.users['yted91']["courses"]["software_engineering"]["assignment1"]["grade"] <= 100;	
