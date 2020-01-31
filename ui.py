"""
CIS 422 Project 1 User Interface

Description: Contains the Tkinter GUI window

Authors: Olivia Pannell, Ben Verney, Joseph Goh

Date Last Modified: 		Last Modified by:		Completed:
1/31/20  					Joseph Goh			    Basic window and structure

TO DO:
* Add always-on-top functionality
    (This should be done at an OS X workstation, as the solution is OS specific)

"""

from tkinter import *
from tkinter import filedialog

listOfNames = ["Bethany", "Mikayla", "Joseph", "Olivia", "Ben"]


# Import filepath and send it to I/O
def imprt():
    filepath = filedialog.askopenfilename(initialdir="./..")
    # send to I/O
    pass


# Export
def exprt():
    pass


# do another thing


def leftPress(event):
    global currentSlot
    if currentSlot == 0:
        return
    listOfSlots[currentSlot].config({"background": "#69779b"})
    listOfSlots[currentSlot].config({"foreground": "White"})
    currentSlot -= 1
    listOfSlots[currentSlot].config({"background": "White"})
    listOfSlots[currentSlot].config({"foreground": "Black"})


def rightPress(event):
    global currentSlot
    if currentSlot == 3:
        return
    listOfSlots[currentSlot].config({"background": "#69779b"})
    listOfSlots[currentSlot].config({"foreground": "White"})
    currentSlot += 1
    listOfSlots[currentSlot].config({"background": "White"})
    listOfSlots[currentSlot].config({"foreground": "Black"})


def upPress(event):
    i = currentSlot
    while i < 3:
        listOfSlots[i].config({"text": listOfSlots[i + 1].cget("text")})
        i += 1
    listOfSlots[3].config({"text": "test"})


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

b2 = Button(win, text="Import", highlightbackground="#002547", padx=10, command=import_file)
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

win.mainloop()
