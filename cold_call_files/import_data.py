"""
CIS 422 Project 1 File I/O

Description: Parses class file
into a list of students and their
information

Date Last Modified: 1/26/20

Authors: Mikayla Campbell, Bethany Van Meter
"""

# this function is for the initial upload of student data
def parse_class_roster(class_roster):
	class_file = open(class_roster, "r")
	number_of_students = 0
	current_student = class_file.readline().strip("\n")
	students = []
	while (current_student):
		one_student = [] # Format -> [first_name, last_name, number, email]
		first_name, last_name, number, email = current_student.split("\t")
		one_student.append(first_name)
		one_student.append(last_name)
		one_student.append(number)
		one_student.append(email)
		students.append(one_student)
		current_student = class_file.readline().strip("\n")
		number_of_students += 1
	return students

# this function loads in previous saves
def load_class_roster_prev_session():
	class_file = open("DO_NOT_TOUCH_class_summary.txt", "r")
	header = class_file.readline()
	current_student = class_file.readline().strip("\n")
	students = []
	while (current_student):
		one_student = [] # Format -> [first_name, last_name, id_num, email, cc_num, flag, flags]
		first_name, last_name, number, email, cc_num, flag, flags = current_student.split("\t")
		one_student.append(first_name)
		one_student.append(last_name)
		one_student.append(number)
		one_student.append(email)
		one_student.append(cc_num)
		one_student.append(flag)
		one_student.append(flags)
		students.append(one_student)
		current_student = class_file.readline().strip("\n")
		number_of_students += 1
	return students
