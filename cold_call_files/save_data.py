"""
CIS 422 Project 1 Save Data

Description: Parses Roster data
into a list of students and their
information and outputs into a text file

Authors: Mikayla Campbell, Bethany Van Meter, Joseph Goh

Last modified by: Joseph Goh

Date last modified: 2/03/20
"""

import csv
from datetime import date

from create_queue import *


# Takes a Roster object and saves it to the designated path, dest_path, as a tab delimited file
def save_roster(roster: Roster, dest_path: str = "DEFAULT-FILEPATH", export: bool = False):
    # Check if dest_path is its default value.
    # If so, set it to roster.filepath (the original roster summary file that was imported)
    if dest_path == "DEFAULT-FILEPATH":
        dest_path = roster.filepath

    # Load all Student objects' summary data into a list of lists for use by csv.writer
    rows = [
        [s.first, s.last, s.id_num, s.email, str(s.cc_ct), str(int(s.flag)), str(s.flag_ct)] for s in roster.students
    ]
    # Write all roster info to dest
    with open(dest_path, "w", newline='') as class_file:
        writer = csv.writer(class_file, dialect='excel-tab', quoting=csv.QUOTE_NONE)
        writer.writerow(["FirstName", "LastName", "ID-Number", "Email", "ColdCallCount", "Flag", "FlagCount"])
        writer.writerows(rows)

    # Save flagged students in a separate file
    flagged_rows = [
        [s.first, s.last, s.id_num, s.email, str(s.cc_ct), str(int(s.flag)), str(s.flag_ct)] for s in roster.flagged
    ]
    with open(dest_path[:-4] + "_flagged.txt", "w", newline='') as flag_file:
        writer = csv.writer(flag_file, dialect='excel-tab', quoting=csv.QUOTE_NONE)
        writer.writerow(["FirstName", "LastName", "ID-Number", "Email", "ColdCallCount", "Flag", "FlagCount"])
        writer.writerows(flagged_rows)

    # Create a session-specific summary-log
    session_rows = []
    for i in range(roster.size):
        s = roster.students[i]
        s_orig = roster.students_orig[i]
        session_rows.append(
            [s.first, s.last, s.id_num, s.email,
             str(s.cc_ct - s_orig.cc_ct), str(int(s.flag) - int(s_orig.flag)), str(s.flag_ct - s_orig.flag_ct)]
        )
    with open(dest_path[:-4] + "_daily.txt", "w", newline='') as daily_file:
        daily_file.write("===========Daily (session) summary for {}==========\n".format(date.today()))
        writer = csv.writer(daily_file, dialect='excel-tab', quoting=csv.QUOTE_NONE)
        writer.writerow(["FirstName", "LastName", "ID-Number", "Email", "ColdCallCount", "Flag", "FlagCount"])
        writer.writerows(session_rows)

    # Save other session info but only if the user is not manually exporting the summary file
    if not export:
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


# Appends record of call/dequeue/flag action to file at log_path, set to log.txt as default
def log_call(student: Student, flagged: bool = False, log_path: str = "log.txt"):
    with open(log_path, "a") as log:
        output = "{} {} ({}) was called for a total of {} times.".format(
            student.first, student.last, student.email, student.cc_ct)
        if flagged:
            output += " The student was also flagged for a total of {} times.".format(student.flag_ct)
        output += "\n"

        log.write(output)


# Appends record of student list import action to file at log_path, set to log.txt as default
def log_import(roster_path: str, log_path: str = "log.txt"):
    with open(log_path, "a") as log:
        output = "Class roster located at \"{}\" imported.\n".format(roster_path)
        log.write(output)


# Appends record of application startup to file at log_path, set to log.txt as default
def log_startup(log_path: str = "log.txt"):
    with open(log_path, "a") as log:
        output = "----------------------------------------\nCold-Call app opened on {}\n".format(date.today())
        log.write(output)
