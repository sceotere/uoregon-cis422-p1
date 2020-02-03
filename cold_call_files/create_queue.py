"""
CIS 422 Project 1 Queue

Description: The object classes for students and student data handling is implemented here.

Authors: Mikayla Campbell, Bethany Van Meter, Joseph Goh

Last modified by: Joseph Goh

Date last modified: 1/31/20

TODO:
    * Deprecate functions not in objects (or integrate as necessary)
    * Design and implement various error handling
"""
# check TODOs

from typing import List
import random
from os import path
import csv

import import_data


class Student:
    def __init__(self, first: str, last: str, id_num: str, email: str, cc_ct: int = 0, flag: bool = False, flag_ct: int = 0):
        # initialize all values.
        # We will end up reading in from a file each of these,
        # so it'll be easy to establish each of the values.
        self.first = first
        self.last = last
        self.id_num = id_num
        self.email = email
        self.cc_ct = cc_ct
        self.flag = flag
        self.flag_ct = flag_ct

    def __str__(self):
        # simple string representation
        return "{} {} [{}, {}]".format(self.first, self.last, self.id_num, self.email)

    def __repr__(self):
        # to show all the values of an instance of a Student
        return "Student({}, {}, {}, {}, {}, {}, {})".format(self.first,
                                                            self.last, self.id_num, self.email, self.cc_ct, self.flag,
                                                            self.flag_ct)

    # Set flag and increment the flag count unless reset arg is set, in which case we clear the flag
    def set_flag(self, reset: bool = False):
        if reset:
            self.flag = False
            self.flag_ct = 0
        else:
            self.flag = True
            self.flag_ct += 1


# Contains the list of Students, as well as the randomizing functionality
class Roster:
    def __init__(self, deck_size: int = 4, filepath: str = "DO_NOT_TOUCH_class_summary.txt", use_conf: bool = False):
        self.filepath = filepath

        self.students = []
        self.flagged = []
        self.size = 0

        self.order = []
        self._next = 0

        self.on_deck = []
        self.deck_size = deck_size

        # TODO: Implement behavior for if class summary file is not found
        # Import the class summary file into memory
        with open(self.filepath, "r", newline='') as class_file:
            reader = csv.reader(class_file, dialect='excel-tab', quoting=csv.QUOTE_NONE)
            # Move past the header
            next(reader)
            for row in reader:
                current_student = Student(row[0], row[1], row[2], row[3], int(row[4]), bool(row[5]), int(row[6]))
                self.students.append(current_student)
                if bool(row[5]):
                    self.flagged.append(current_student)
                self.size += 1

        # First, do the default build of self.order
        for i in range(self.size):
            self.order.append(i)

        # Check for config data saved from previous sessions and fill deck accordingly
        # Check saved coldcall.ini if we're restoring from a previous session.
        if use_conf:
            with open("coldcall.ini", "r") as conf_file:
                # Check the file path, see if it's valid and properly formatted'.
                # If not, this config is outdated so do the default init
                path_line = conf_file.readline().strip("\n").split("=")
                if len(path_line) == 2 and path.exists(path_line[1]) and path_line[1] == self.filepath:
                    # The text after the equals sign, split by commas, then converted to ints, put into a list
                    saved_deck = [int(i) for i in conf_file.readline().strip("\n").split("=")[1].split(",")]
                    if self.deck_size == len(saved_deck):
                        self.on_deck = saved_deck

                    # Check for saved shuffled order and load it if its length is valid
                    if path.exists("order.txt"):
                        with open("order.txt", "r") as order_file:
                            # The items of the line, converted to ints, then put back into a list
                            saved_order = [int(i) for i in order_file.readline().strip("\n").split("\t")]
                            if len(saved_order) == self.size:
                                self.order = saved_order

                    # Grab next up index
                    self._next = int(conf_file.readline().strip("\n").split("=")[1])
                else:
                    self.shuffle()
                    for i in range(self.deck_size):
                        self.on_deck.append(self.get_next_idx())
        # If we're not using config data, just shuffle and build the deck to finish
        else:
            self.shuffle()
            for i in range(self.deck_size):
                self.on_deck.append(self.get_next_idx())

    def __repr__(self):
        return "Roster({})".format(self.size)

    def shuffle(self):
        random.shuffle(self.order)
        self._next = 0

    def get_next_idx(self) -> int:
        # If the next-index is larger than our entire roster, then we have an error
        if self._next > self.size:
            raise IndexError("The roster feed is out of bounds!")
        # If we reached the end of the list, reshuffle the list
        elif self._next == self.size:
            self.shuffle()

        # Save the student index to be returned
        ret = self.order[self._next]
        # Increment the next-index
        self._next += 1

        # If the roster doesn't contain enough students to prevent duplicates on deck, so be it. Just return.
        if self.deck_size >= self.size:
            return ret
        # Else, check if the student being returned is already on deck. Loop for one that isn't til we find one.
        else:
            while ret in self.on_deck:
                # Shuffle if we've reached the end of the list
                if self._next == self.size:
                    self.shuffle()
                # Save the student index to be returned
                ret = self.order[self._next]
                # Increment the next-index
                self._next += 1

        return ret

    # Get the nth Student on deck
    def get_student(self, n: int, from_deck: bool = True):
        if from_deck:
            return self.students[self.on_deck[n]]
        else:
            return self.students[n]

    # Dequeue the nth Student on deck, grab the next one, and then return the dequeued Student
    def dequeue(self, n: int, flag: bool = False) -> Student:
        to_dequeue = self.students[self.on_deck[n]]
        to_dequeue.cc_ct += 1
        # If the instructor is flagging the student, take appropriate actions
        if flag:
            # If the student hasn't been flagged already, append them to the roster's flagged list
            if not to_dequeue.flag:
                self.flagged.append(to_dequeue)
            to_dequeue.set_flag()
        # Shift all the entries down 1, and add a new person on the end
        i = n
        while i < 3:
            self.on_deck[i] = self.on_deck[i+1]
            i += 1
        self.on_deck[3] = self.get_next_idx()


        return to_dequeue

    def save_state(self):
        # Update the class summary
        rows = [
            [s.first, s.last, s.id_num, s.email, str(s.cc_ct), str(int(s.flag)), str(s.flag_ct)] for s in self.students
        ]
        with open(self.filepath, "w", newline='') as class_file:
            writer = csv.writer(class_file, dialect='excel-tab', quoting=csv.QUOTE_NONE)
            writer.writerow(["FirstName", "LastName", "ID-Number", "Email", "ColdCallCount", "Flag", "FlagCount"])
            writer.writerows(rows)

        # Create/Update the summary of flagged students
        flagged_rows = [
            [s.first, s.last, s.id_num, s.email, str(s.cc_ct), str(int(s.flag)), str(s.flag_ct)] for s in self.flagged
        ]
        with open(self.filepath[:-3] + "_flags.txt", "w", newline='') as flag_file:
            writer = csv.writer(flag_file, dialect='excel-tab', quoting=csv.QUOTE_NONE)
            writer.writerow(["FirstName", "LastName", "ID-Number", "Email", "ColdCallCount", "Flag", "FlagCount"])
            writer.writerows(flagged_rows)

        # Store the current shuffled order of student indices
        order_row = [str(idx) for idx in self.order]
        with open("order.txt", "w", newline='') as order_file:
            writer = csv.writer(order_file, dialect='excel-tab', quoting=csv.QUOTE_NONE)
            writer.writerow(order_row)

        # Store other session state info in config file
        with open("coldcall.ini", "w") as conf_file:
            conf_file.write("rosterpath=" + self.filepath + "\n")
            conf_file.write("ondeck=" + ",".join([str(idx) for idx in self.on_deck]) + "\n")
            conf_file.write("nextindex=" + str(self._next) + "\n")


# TODO: Deprecate this
def build_roster(summary_path: str = "DO_NOT_TOUCH_class_summary.txt") -> List[Student]:
    current_class = []
    if path.exists(summary_path):
        # test class for small testing
        current_class = [["Mikayla", "Campbell", 904895018, "mikayla@gmail.com"],
                         ["Billy", "Bob", 893028490, "billy@gmail.com"],
                         ["John", "Doe", 390847638, "john@gmail.com"],
                         ["Sarah", "Davis", 278938475, "sarah@gmail.com"],
                         ["Beth", "Lee", 904895098, "beth@gmail.com"]]
    else:
        current_class = import_data.parse_class_roster("test_class.txt")

    class_roster = []
    for student_info in current_class:
        # create a student
        current_student = Student(student_info[0],
                                  student_info[1], student_info[2], student_info[3], 0, 0, 0)
        # append that created student to the roster
        class_roster.append(current_student)

    # return the created roster
    return class_roster


# TODO: Deprecate this
def randomize_li(class_li):
    # use Python's built in shuffle function
    random.shuffle(class_li)
    return class_li


# TODO: Deprecate this
# for the initial creation of the "on deck" queue
def make_q(class_li):
    # each queue has 4 "on deck" students

    # create a queue with 4 "empty" spots
    q = [None, None, None, None]

    # ensure the roster passed in is not empty
    if class_li is not None:
        # 4 because it's the queue "on deck" size
        for i in range(4):
            q[i] = class_li[i]
        # after adding to smaller queue, set the leftover students to list
        # of remaining students from original list
        class_li_short = class_li[4:]
    # return the "on deck" queue and the remaining students in the larger queue not shown
    return q, class_li_short


# TODO: Deprecate this
# remove the student the user wants to remove and returns a 3 student list
# (acts as a shift after removal)
# TODO: determine here if the removal was flagged or not
def shift_q(num, q):
    # remove the student in the queue at num position but also increase the cc_num (cold call number)
    q[num].cc_num += 1
    q.remove(q[num])
    # return the on deck queue list of remaining students
    return q


# TODO: Deprecate this
# adds a student to the end of the queue
def add_to_q(q, class_li):
    # if class_li (students not called yet) is empty, fill it again
    if class_li is None or len(class_li) == 0:
        class_li = build_roster()
        class_li = randomize_li(class_li)

    # until we have added a student, keep looking for one not in the queue yet (count with i)
    class_li_short = class_li
    i = 0
    # while we haven't added a student to the on deck queue
    while len(q) < 4:
        # if the student we are trying to add is already in the "on deck" queue,
        # continue looking for another to add
        if class_li_short[i].id_num == q[0].id_num \
                or class_li_short[i].id_num == q[1].id_num \
                or class_li_short[i].id_num == q[2].id_num:
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
    cis422 = build_roster("test_class.txt")
    cis422_rand = cis422[:]
    cis422_rand = randomize_li(cis422_rand)

    # all random students in one queue
    print("all random students in one queue")
    print(cis422_rand)
    print("\n\n\n")

    cis422_q, cis422_rand = make_q(cis422_rand)

    # print the on deck queue followed by the students remaining in the queue (without adding)
    print("the on deck queue followed by the students remaining in the queue (without adding)\n")
    print("On deck queue: \n", cis422_q)
    print("\nRemaining students to add to on deck queue:\n", cis422_rand)
    print("\n\n\n")

    # print the removal of a student from the on deck queue:
    print("the removal of a student from the on deck queue (num = 1):\n")
    q_shift = shift_q(1, cis422_q)
    print(q_shift)
    print("\n\n\n")

    # print the on deck queue and students remaining after adding from the queue left over:
    q_2, cis422_rand2 = add_to_q(q_shift, cis422_rand)

    print("the on deck queue and students remaining after adding from the queue left over:\n\n",
          q_2, "\n\nQueue left over:\n", cis422_rand2)
    print("\n\n\n")

    print("the removal of a student from the on deck queue (num = 1):\n")
    q_shift2 = shift_q(1, q_2)
    print(q_shift2)
    print("\n\n\n")

    q_3, cis422rand3 = add_to_q(q_shift2, cis422_rand2)
    print("the on deck queue and students remaining after adding from the queue left over:\n\n",
          q_3, "\n\nQueue left over:\n", cis422rand3)
    print("\n\n\n")


if __name__ == "__main__":
    main()
