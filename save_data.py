"""
CIS 422 Project 1 Save Data

Description: 

Date Last Modified: 1/27/20

Authors: Mikayla Campbell, Bethany Van Meter
"""

# Clean up and add comments

from os import path


def save_term_summary(class_roster, class_name):
    if path.exists("DO_NOT_TOUCH{}_class_summary.txt".format(class_name)):

        class_file = open("DO_NOT_TOUCH{}_class_summary.txt".format(class_name), "r")
        output = []
        current_line = class_file.readline()
        output.append(current_line)
        current_line = class_file.readline()
        output.append(current_line)
        current_line = class_file.readline().strip("\n")

        students_used = []

        while current_line:
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

        while current_line:
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
