"""
CIS 422 Project 1 Queue

Description: 

Date Last Modified: 1/25/20

Authors: Mikayla Campbell, Bethany Van Meter
"""
import random

class Student:
	def __init__(self, first, last, id_num, email, cc_num, flag, num_flags):
		self.first = first
		self.last = last
		self.id_num = id_num
		self.email = email
		self.cc_num = cc_num
		self.flag = flag
		self.num_flags = num_flags

	def __str__(self):
		return "[{}, {}, {}, {}]".format(self.first, self.last, self.id_num, self.email)

	def __repr__(self):
		return "Student({}, {}, {}, {}, {}, {}, {})".format(self.first,
			self.last, self.id_num, self.email, self.cc_num, self.flag, self.num_flags)

def create_class():
	test_class = [["Mikayla", "Campbell", 904895098, "mikayla@gmail.com"],
		["Billy", "Bob", 893028490, "billy@gmail.com"],
		["John", "Doe", 390847638, "john@gmail.com"],
		["Sarah", "Davis", 278938475, "sarah@gmail.com"],
		["Beth", "Lee", 904895098, "beth@gmail.com"]]

	class_roster = []
	for student_info in test_class:
		current_student = Student(student_info[0],
			student_info[1], student_info[2], student_info[3], 0, 0, 0)
		class_roster.append(current_student)

	return class_roster

def randomize_li(class_li):
	random.shuffle(class_li)
	return class_li

def make_q(class_li):
	q = [None, None, None, None]
	if class_li != None:
		for i in range(4):
			q[i] = class_li[i]
		class_li_short = class_li[3:]
	return q, class_li_short

def shift_q(num, q):
	q.remove(q[num])
	return q

def add_to_q(q, class_li):
	q.append(class_li[0])
	class_li_short = class_li[1:]
	return q, class_li_short

def main():
	CIS422 = create_class()
	CIS422_rand = CIS422[:]
	CIS422_rand = randomize_li(CIS422_rand)
	CIS422_q, CIS422_rand = make_q(CIS422_rand)
	q_shift = shift_q(1, CIS422_q)
	q_2, CIS422_rand2 = add_to_q(q_shift, CIS422_rand)

	print(q_shift)
	print("\n\n\n")
	print(q_2)
	print("\n\n\n")
	print(CIS422_rand)
	print("\n\n\n")
	print(CIS422_rand2)

if __name__ == "__main__":
	main()