"""
CIS 422 Project 1 Save Data

Description: 

Date Last Modified: 1/26/20

Authors: Mikayla Campbell, Bethany Van Meter
"""

# save the class roster with current information
def save_class_roster(class_roster):
    class_file = open("DO_NOT_TOUCH_class_summary.txt", "w")
    class_file.write("Class Summary\n")
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
    return None

# TODO: save not the summary but the daily log.. how should we?
