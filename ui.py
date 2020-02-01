"""
CIS 422 Project 1 User Interface

Description: Contains the Tkinter GUI window

Authors: Olivia Pannell, Ben Verney, Joseph Goh

Date Last Modified: 		Last Modified by:		Completed:
1/31/20  					Joseph Goh			    Basic window and structure

TODO:
* Change name labels to use StringVars instead of regular strings, so that they can be automatically updated
* Add always-on-top functionality
    (This should be done at an OS X workstation, as the solution is OS specific)

"""

from tkinter import *
from tkinter import filedialog

from create_queue import *

global roster
global currentSlot
global listOfNames
global listOfSlots

# Import filepath and return it for use
def imprt():
    global currentSlot
    global listOfNames
    global listOfSlots

    filepath = filedialog.askopenfilename(initialdir="./..")
    if path.exists(filepath):
        roster = Roster(filepath=filepath)
        for i in range(4):
            current_student = roster.students[roster.on_deck[i]]
            listOfNames[i] = current_student.first + " " + current_student.last[0] + "."

# Export
def exprt():
    pass


# do another thing


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
    pass


def downPress(event):
    global roster
    global currentSlot
    global listOfNames
    global listOfSlots
    pass


# Initialize listOfNames
listOfNames = [StringVar(), StringVar(), StringVar(), StringVar()]
listOfNames[0].set("Press")
listOfNames[1].set("the")
listOfNames[2].set("Import")
listOfNames[3].set("Button!")

# Try to initialize Roster and listOfNames and deck if we have a previous session already saved
if path.exists("coldcall.ini"):
    with open("coldcall.ini", "r") as conf_file:
        conf_filepath = conf_file.readline()
        if path.exists(conf_filepath):
            roster = Roster(filepath=conf_filepath)
            for i in range(4):
                current_student = roster.students[roster.on_deck[i]]
                listOfNames[i] = current_student.first + " " + current_student.last[0] + "."

# sets window size and background color
win = Tk()
win.geometry("350x150")
win.config(bg="#002547")

# win.iconbitmap()
# do this if I have time.

# Title of the window
win.title("422 Cold Call")

# Labels and Buttons
lbl1 = Label(win, text='On Deck:', bg="#002547", fg="white", font=("Arial", 16))
lbl1.grid(row=0, column=1, padx=5, pady=5)

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

b2 = Button(win, text="Import", highlightbackground="#002547", padx=10, command=imprt)
b2.place(relx=0.0, rely=1.0, anchor=SW)

b3 = Button(win, text="Export", highlightbackground="#002547", padx=10, command=exprt)
b3.place(relx=0.20, rely=1.0, anchor=SW)

listOfSlots = [slot0, slot1, slot2, slot3]
currentNames = [0, 1, 2, 3]
currentSlot = 0
slot0.config({"background": "White"})
slot0.config({"foreground": "Black"})

win.bind('<Left>', leftPress)
win.bind('<Right>', rightPress)
win.bind('<Up>', upPress)
win.bind('<Down>', downPress)

win.mainloop()
