"""
CIS 422 Project 1 Save Data

Description: 

Date Last Modified: 1/26/20

Authors: Mikayla Campbell, Bethany Van Meter
"""

# save the class roster with current information

# FIX TODOS

import os.path
from os import path

# for this function I think we should 
    # 1) Add to a students summary if it is already
    #    there
    # 2) Update flag, num_flags, and cc_num to 0 after
    #    each use
    # *** This way these variables can be used for the daily log ***
    # *** and we won't have to make new variables for those ***
def save_class_roster(class_roster, class_name):
    if path.exists("DO_NOT_TOUCH{}_class_summary.txt"\
        .format(class_name)):

        class_file = open("DO_NOT_TOUCH{}_class_summary.txt"\
            .format(class_name), "w")
        current_line = class_file.readline()
        current_line = class_file.readline()

        while (current_line):
            current_student = class_file.readline().strip("\n")
            first_name, last_name, number, email, cc_num,
                flag, flags = current_student.split("\t")
            for student in class_roster:
                if student.number == number:
                    if student.cc_num != 0 and student.num_flags != 0:
                        student.cc_num += cc_num
                        student.num_flags += flags
                        class_file.write(current_line.replace(current_line,
                            "{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(student.first,
                            student.last, student.id_num, student.email,
                            student.cc_num, student.flag, student.num_flags)))
                    break
    else:
        class_file = open("DO_NOT_TOUCH{}_class_summary.txt"\
            .format(class_name), "w")
        class_file.write("{} Summary\n".format(class_name))
        class_file.write("first", "\t",
                             "last", "\t",
                             "id_num", "\t",
                             "email", "\t",
                             "cc_num", "\t",
                             "flag", "\t",
                             "flags", "\t\n")

        # for each student in the whole roster, save their data
        for student in class_roster:
                class_file.write(student.first, "\t",
                     student.last, "\t",
                     student.id_num, "\t",
                     student.email, "\t",
                     student.cc_num, "\t",
                     student.flag, "\t",
                     student.num_flags, "\t\n")
    class_file.close()

    for student in class_roster:
        student.cc_num = 0
        student.flag = 0
        student.num_flags = 0
    return None

# TODO: save not the summary but the daily log...how should we?

def save_daily_log(class_roster, class_name):
    class_file = open("DO_NOT_TOUCH{}_daily_log.txt"\
        .format(class_name), "w")

    # for each student in the whole roster, save their data
    for student in class_roster:
        if student.cc_num != 0 or student.flag != 0:
            class_file.write(student.first, "\t",
                 student.last, "\t",
                 student.id_num, "\t",
                 student.email, "\t",
                 student.cc_num, "\t",
                 student.flag, "\t",
                 student.num_flags, "\t\n")
    class_file.close()
    return None
