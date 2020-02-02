"""
CIS 422 Project 1 Save Data

Description: Parses class file
into a list of students and their
information

Authors: Mikayla Campbell, Bethany Van Meter

Last modified by: Joseph Goh

Date last modified: 1/31/20
"""

# Clean up and add comments

from create_queue import *
from datetime import date


def save_roster(roster: Roster):
    # Update the class summary
    rows = [
        [s.first, s.last, s.id_num, s.email, str(s.cc_ct), str(int(s.flag)), str(s.flag_ct)] for s in roster.students
    ]
    with open(roster.filepath, "w", newline='') as class_file:
        writer = csv.writer(class_file, dialect='excel-tab', quoting=csv.QUOTE_NONE)
        writer.writerow(["FirstName", "LastName", "ID-Number", "Email", "ColdCallCount", "Flag", "FlagCount"])
        writer.writerows(rows)

    # Create/Update the summary of flagged students
    flagged_rows = [
        [s.first, s.last, s.id_num, s.email, str(s.cc_ct), str(int(s.flag)), str(s.flag_ct)] for s in roster.flagged
    ]
    with open(roster.filepath[:-3] + "_flags.txt", "w", newline='') as flag_file:
        writer = csv.writer(flag_file, dialect='excel-tab', quoting=csv.QUOTE_NONE)
        writer.writerow(["FirstName", "LastName", "ID-Number", "Email", "ColdCallCount", "Flag", "FlagCount"])
        writer.writerows(flagged_rows)

    # Store the current shuffled order of student indices
    order_row = [str(idx) for idx in roster.order]
    with open("order.txt", "w", newline='') as order_file:
        writer = csv.writer(order_file, dialect='excel-tab', quoting=csv.QUOTE_NONE)
        writer.writerow(order_row)

    # Store other session state info in config file
    with open("coldcall.ini", "w") as conf_file:
        conf_file.write("rosterpath=" + roster.filepath + "\n")
        conf_file.write("ondeck=" + ",".join([str(idx) for idx in roster.on_deck]) + "\n")
        conf_file.write("nextindex=" + str(roster._next) + "\n")


def log_call(student: Student, flagged: bool = False, log_path: str = "log.txt"):
    with open(log_path, "a") as log:
        output = f"{student.first} {student.last} ({student.email}) was called for a total of {student.cc_ct} times."
        if flagged:
            output += f" The student was also flagged for a total of {student.flag_ct} times."
        output += "\n"

        log.write(output)


def log_import(roster_path: str, log_path: str = "log.txt"):
    with open(log_path, "a") as log:
        output = f"Class roster located at \"{roster_path}\" imported.\n"
        log.write(output)


def log_startup(log_path: str = "log.txt"):
    with open(log_path, "a") as log:
        output = f"Cold-Call app opened on {date.today()}\n"
        log.write(output)


def save_term_summary(class_roster, class_name):
    if path.exists("DO_NOT_TOUCH{}_class_summary.txt" \
                           .format(class_name)):

        class_file = open("DO_NOT_TOUCH{}_class_summary.txt" \
                          .format(class_name), "r")
        output = []
        current_line = class_file.readline()
        output.append(current_line)
        current_line = class_file.readline()
        output.append(current_line)
        current_line = class_file.readline().strip("\n")

        students_used = []

        while (current_line):
            first_name, last_name, number, email, cc_num, flags = current_line.split("\t")
            for student in class_roster:
                if student.id_num == int(number):
                    if student.id_num not in students_used:
                        student.cc_num += int(cc_num)
                        student.num_flags += int(flags)
                        write_str = student.first + "\t" + \
                                    student.last + "\t" + \
                                    str(student.id_num) + "\t" + \
                                    student.email + "\t" + \
                                    str(student.cc_num) + "\t" + \
                                    str(student.num_flags) + "\n"
                        output.append(write_str)
                        students_used.append(int(number))
                    break
            current_line = class_file.readline().strip("\n")

        class_file.seek(0)
        current_line = class_file.readline()
        current_line = class_file.readline()
        current_line = class_file.readline().strip("\n")

        while (current_line):
            first_name, last_name, number, email, cc_num, flags = current_line.split("\t")
            for student in class_roster:
                if student.id_num == number and number not in students_used:
                    write_str = current_line + "\n"
                    output.append(write_str)
                    students_used.append(int(number))
            current_line = class_file.readline().strip("\n")

        class_file2 = open("DO_NOT_TOUCH{}_class_summary.txt" \
                           .format(class_name), "w")
        class_file2.writelines(output)
    else:
        class_file = open("DO_NOT_TOUCH{}_class_summary.txt" \
                          .format(class_name), "w+")
        class_file.write("{} Summary\n".format(class_name))
        class_file.write("first\tlast\tid_num\temail\tcc_num\tflags\t\n")

        # for each student in the whole roster, save their data
        for student in class_roster:
            write_str = student.first + "\t" + \
                        student.last + "\t" + \
                        str(student.id_num) + "\t" + \
                        student.email + "\t" + \
                        str(student.cc_num) + "\t" + \
                        str(student.num_flags) + "\n"
            class_file.write(write_str)
    class_file.close()

    for student in class_roster:
        student.cc_num = 0
        student.num_flags = 0
    return None


# TODO: save not the summary but the daily log...how should we?

def save_daily_log(class_roster, class_name):
    class_file = open("DO_NOT_TOUCH{}_daily_log.txt" \
                      .format(class_name), "w")

    # for each student in the whole roster, save their data
    for student in class_roster:
        if student.cc_num != 0 or student.num_flags != 0:
            write_str = student.first + "\t" + \
                        student.last + "\t" + \
                        str(student.id_num) + "\t" + \
                        student.email + "\t" + \
                        str(student.cc_num) + "\t" + \
                        str(student.num_flags) + "\n"
            class_file.write(write_str)
    class_file.close()
    return None


def save_queue(queue, class_roster, class_name):
    class_file = open("DO_NOT_TOUCH{}_saved_state.txt" \
                      .format(class_name), "w")
    write_str = str(queue) + "\n" + str(class_roster) + "\n"
    class_file.write(write_str)
    return None
