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
