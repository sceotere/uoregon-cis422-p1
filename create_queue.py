"""
CIS 422 Project 1 Queue

Description: 

Date Last Modified: 1/26/20

Authors: Mikayla Campbell, Bethany Van Meter
"""
#check TODOs

import io
import random
import os.path
from os import path

class Student:
	def __init__(self, first, last, id_num, email, cc_num, flag, num_flags):
                # initialize all values.
                # We will end up reading in from a file each of these,
                # so it'll be easy to establish each of the values.
		self.first = first
		self.last = last
		self.id_num = id_num
		self.email = email
		self.cc_num = cc_num
		self.flag = flag
		self.num_flags = num_flags

	def __str__(self):
                # simple string representation
		return "[{}, {}, {}, {}]".format(self.first, self.last, self.id_num, self.email)

	def __repr__(self):
                # to show all the values of an instance of a Student
		return "Student({}, {}, {}, {}, {}, {}, {})".format(self.first,
			self.last, self.id_num, self.email, self.cc_num, self.flag, self.num_flags)

# TODO: change to create the class from file input
def create_class(class_roster):
	current_class = []
	if path.exists("DO_NOT_TOUCH_class_summary.txt"):
		   # test class for small testing
		current_class = [["Mikayla", "Campbell", 904895018, "mikayla@gmail.com"],
			["Billy", "Bob", 893028490, "billy@gmail.com"],
			["John", "Doe", 390847638, "john@gmail.com"],
			["Sarah", "Davis", 278938475, "sarah@gmail.com"],
			["Beth", "Lee", 904895098, "beth@gmail.com"]]
	else:
		current_class = io.parse_class_roster("test_class.txt")

	class_roster = []
	for student_info in test_class:
                # create a student
		current_student = Student(student_info[0],
			student_info[1], student_info[2], student_info[3], 0, 0, 0)
		# append that created student to the roster
		class_roster.append(current_student)

        # return the created roster
	return class_roster

def randomize_li(class_li):
        # use Python's built in shuffle function
	random.shuffle(class_li)
	return class_li

# for the initial creation of the "on deck" queue
def make_q(class_li):
        # each queue has 4 "on deck" students

        #create a queue with 4 "empty" spots
	q = [None, None, None, None]

	#ensure the roster passed in is not empty
	if class_li != None:
                # 4 because it's the queue "on deck" size
		for i in range(4):
			q[i] = class_li[i]
		# after adding to smaller queue, set the leftover students to list
		# of remaining students from original list
		class_li_short = class_li[4:]
	# return the "on deck" queue and the remaining students in the larger queue not shown
	return q, class_li_short

# remove the student the user wants to remove and returns a 3 student list
#(acts as a shift after removal)
# TODO: determine here if the removal was flagged or not
def shift_q(num, q):
        # remove the student in the queue at num position but also increase the cc_num (cold call number)
        q[num].cc_num += 1
        q.remove(q[num])
        # return the on deck queue list of remaining students
        return q

# adds a student to the end of the queue
def add_to_q(q, class_li):
        # if class_li (students not called yet) is empty, fill it again
        if class_li == None or len(class_li) == 0:
                class_li = create_class()
                class_li = randomize_li(class_li)

        # until we have added a student, keep looking for one not in the queue yet (count with i)
        class_li_short = class_li
        i = 0
        # while we haven't added a student to the on deck queue
        while(len(q) < 4):
                # if the student we are trying to add is already in the "on deck" queue,
                # continue looking for another to add
                if(class_li_short[i].id_num == q[0].id_num or\
                	class_li_short[i].id_num == q[1].id_num or class_li_short[i].id_num == q[2].id_num):
                        i += 1
                # else, the student we are trying to add isn't in the on deck" queue
                else:
                        # append the student to the end of the "on deck" queue
                        # and that student is removed from not "on deck" queue by the pop method
                        q.append(class_li_short.pop(i))
        
        # return the on deck queue and rest of students in the not "on deck" queue
        # not on deck student list may be empty. This is expected
        return q, class_li_short

def main():
        CIS422 = create_class()
        CIS422_rand = CIS422[:]
        CIS422_rand = randomize_li(CIS422_rand)

        # all random students in one queue
        print("all random students in one queue")
        print(CIS422_rand)
        print("\n\n\n")
        
        CIS422_q, CIS422_rand = make_q(CIS422_rand)

        # print the on deck queue followed by the students remaining in the queue (without adding)
        print("the on deck queue followed by the students remaining in the queue (without adding)\n")
        print("On deck queue: \n", CIS422_q)
        print("\nRemaining students to add to on deck queue:\n", CIS422_rand)
        print("\n\n\n")

        # print the removal of a student from the on deck queue:
        print("the removal of a student from the on deck queue (num = 1):\n")
        q_shift = shift_q(1, CIS422_q)
        print(q_shift)
        print("\n\n\n")
        
        # print the on deck queue and students remaining after adding from the queue left over:
        q_2, CIS422_rand2 = add_to_q(q_shift, CIS422_rand)
        
        print("the on deck queue and students remaining after adding from the queue left over:\n\n",
        	q_2, "\n\nQueue left over:\n", CIS422_rand2)
        print("\n\n\n")

        print("the removal of a student from the on deck queue (num = 1):\n")
        q_shift2 = shift_q(1, q_2)
        print(q_shift2)
        print("\n\n\n")
        
        q_3, CIS422rand3 = add_to_q(q_shift2, CIS422_rand2)
        print("the on deck queue and students remaining after adding from the queue left over:\n\n",
        	q_3, "\n\nQueue left over:\n", CIS422rand3)
        print("\n\n\n")

        
if __name__ == "__main__":
	main()
