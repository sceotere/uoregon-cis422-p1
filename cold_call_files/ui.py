"""
CIS 422 Project 1 User Interface

Description: Contains the Tkinter GUI window

Authors: Olivia Pannell, Ben Verney, Joseph Goh

Date Last Modified: 		Last Modified by:		Completed:
2/03/20  					Joseph Goh			    Most functionality

TODO: Update comments

"""

from tkinter import *
from tkinter import filedialog
from os import path

from create_queue import *
from save_data import *


def update_ui():
    global listOfNames
    global listOfSlots
    global roster
    for i in range(4):
        current_student = roster.get_student(i)
        listOfNames[i] = current_student.first + " " + current_student.last[0] + "."
        listOfSlots[i].config({"text": listOfNames[i]})


# Import filepath and return it for use
def imprt():
    global roster

    filepath = filedialog.askopenfilename(initialdir="./..")
    if path.exists(filepath):
        roster = Roster(filepath=filepath)
        update_ui()
        save_roster(roster)
        log_import(filepath)


# Export
def exprt():
    global roster

    filepath = filedialog.asksaveasfilename(initialdir="./..")
    save_roster(roster, filepath, export=True)


# Reset the flags of all the students in the currently loaded roster
def reset_flags():
    global roster
    for i in range(roster.size):
        roster.students[i].set_flag(reset=True)
    save_roster(roster)


def leftPress(event):
    global currentSlot
    global listOfNames
    global listOfSlots
    if currentSlot == 0:
        return
    listOfSlots[currentSlot].config({"background": "#69779b"})
    listOfSlots[currentSlot].config({"foreground": "White"})
    currentSlot -= 1
    listOfSlots[currentSlot].config({"background": "White"})
    listOfSlots[currentSlot].config({"foreground": "Black"})


def rightPress(event):
    global currentSlot
    global listOfNames
    global listOfSlots
    if currentSlot == 3:
        return
    listOfSlots[currentSlot].config({"background": "#69779b"})
    listOfSlots[currentSlot].config({"foreground": "White"})
    currentSlot += 1
    listOfSlots[currentSlot].config({"background": "White"})
    listOfSlots[currentSlot].config({"foreground": "Black"})


def upPress(event):
    global roster
    global currentSlot
    global listOfNames
    global listOfSlots
    dequeued = roster.dequeue(currentSlot, False)
    update_ui()
    save_roster(roster)
    log_call(dequeued)


def downPress(event):
    global roster
    global currentSlot
    global listOfNames
    global listOfSlots
    dequeued = roster.dequeue(currentSlot, True)
    update_ui()
    save_roster(roster)
    log_call(dequeued, flagged=True)


log_startup()

roster = None
listOfNames = ["Press", "the", "Import", "Button!"]

# Try to initialize Roster and listOfNames and deck if we have a previous session already saved
if path.exists("coldcall.ini"):
    with open("coldcall.ini", "r") as conf_file:
        conf_filepath = conf_file.readline().strip("\n").split("=")[1]
        print(f"Attempting to load previous session from: {conf_filepath}")
        if path.exists(conf_filepath):
            roster = Roster(filepath=conf_filepath, use_conf=True)
            log_import(conf_filepath)

# sets window size and background color
win = Tk()
win.geometry("350x150")
win.config(bg="#002547")
win.resizable(True, False)
win.attributes('-topmost', 'true')

# win.iconbitmap()
# do this if I have time.

# Title of the window
win.title("422 Cold Call")

# Labels and Buttons
lbl1 = Label(win, text='On Deck:', bg="#002547", fg="white", font=("Arial", 16))
lbl1.grid(row=0, column=1, padx=5, pady=5, sticky=W)

slot0 = Label(win, text=listOfNames[0], bg="#69779b", fg="white", padx=10,
              relief=RAISED)  # Not sure if we like RAISED or SUNKEN
slot0.grid(row=1, column=1, padx=5, pady=5)

slot1 = Label(win, text=listOfNames[1], bg="#69779b", fg="white", padx=10, relief=RAISED)
slot1.grid(row=1, column=2, padx=5, pady=5)

slot2 = Label(win, text=listOfNames[2], bg="#69779b", fg="white", padx=10, relief=RAISED)
slot2.grid(row=1, column=3, padx=5, pady=5)

slot3 = Label(win, text=listOfNames[3], bg="#69779b", fg="white", padx=10, relief=RAISED)
slot3.grid(row=1, column=4, padx=5, pady=5)

lbl2 = Label(win, text="Help: \nDequeue - up\nFlag - down", bg="#002547", fg="white", font=("Arial", 12))
lbl2.place(relx=1.0, rely=1.0, anchor=SE)

b0 = Button(win, text="Import", highlightbackground="#002547", padx=10, command=imprt)
b0.place(relx=0.0, rely=1.0, anchor=SW)

b1 = Button(win, text="Export", highlightbackground="#002547", padx=10, command=exprt)
b1.place(relx=0.20, rely=1.0, anchor=SW)

b2 = Button(win, text="Reset Flags", highlightbackground="#002547", padx=10, command=reset_flags)
b2.place(relx=0.40, rely=1.0, anchor=SW)

listOfSlots = [slot0, slot1, slot2, slot3]
currentNames = [0, 1, 2, 3]
currentSlot = 0
slot0.config({"background": "White"})
slot0.config({"foreground": "Black"})

win.bind('<Left>', leftPress)
win.bind('<Right>', rightPress)
win.bind('<Up>', upPress)
win.bind('<Down>', downPress)

if roster is None:
    for i in range(4):
        listOfSlots[i].config({"text": listOfNames[i]})
else:
    update_ui()


win.mainloop()
