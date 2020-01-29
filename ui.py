"""
CIS 422 Project 1 User Interface

Description: 

Date Last Modified: 		Last Modified by:		Completed:
1/23/20  					Olivia Pannell			Basic window and structure
"""

from tkinter import *
from tkinter import filedialog

listOfNames = ["Bethany", "Mikayla", "Joseph", "Olivia", "Ben"]


# Button Commands
def hlp():
	pass
	#do something here

def imprt():
	filepath = filedialog.askopenfilename(initialdir="./..")
	pass
	#do something here

def exprt():
	pass
	#do another thing

#Structure of the main menu
def construct():
	pass
	#will come back to this -op

#sets window size and background color
win = Tk()
win.geometry("350x150")
win.config(bg="#002547") #dark slate gray

#win.iconbitmap()
#do this if I have time.

#title of the window
win.title("422 Cold Call")

#labels and buttons
lbl1 = Label(win, text='On Deck:', bg = "#002547", fg= "white", font=("Arial", 16))
lbl1.grid(row = 0, column = 1, padx=5, pady=5)

slot0 =Label(win, text = listOfNames[0], highlightbackground = "#002547", padx = 10)
slot0.grid(row = 1, column = 1, padx=5, pady=5)

slot1 =Label(win, text = listOfNames[1], highlightbackground = "#002547", padx = 10, anchor = N) 
slot1.grid(row = 1, column = 2, padx=5, pady=5)

slot2 =Label(win, text = listOfNames[2], highlightbackground = "#002547", padx = 10, anchor = N) 
slot2.grid(row = 1, column = 3, padx=5, pady=5)

slot3 =Label(win, text = listOfNames[3], highlightbackground = "#002547", padx = 10, anchor = N) 
slot3.grid(row = 1, column = 4, padx=5, pady=5)

b1 =Button(win, text = "help", highlightbackground = "#002547", padx = 10, command = hlp)
b1.place(relx=1.0, rely=1.0, anchor=SE)

b2 = Button(win, text = "import", highlightbackground = "#002547", padx = 10, command = imprt)
b2.place(relx=0.0, rely=1.0, anchor=SW)

b3 = Button(win, text = "export", highlightbackground = "#002547", padx = 10, command = exprt)
b3.place(relx=0.20, rely=1.0, anchor=SW)


# ent2 = Entry()
# lbl2.grid(column=0, row=1, padx=5, pady=5)
# ent2.grid(column=1, row=1, padx=5, pady=5)

listOfSlots = [slot0, slot1, slot2, slot3]
currentNames = [0,1,2,3]
currentSlot = 0
slot0.config({"background": "Blue"})
slot0.config({"foreground": "White"})

def leftPress(event):
	global currentSlot
	if currentSlot == 0:
		return
	listOfSlots[currentSlot].config({"background": "White"})
	listOfSlots[currentSlot].config({"foreground": "Black"})
	currentSlot -= 1
	listOfSlots[currentSlot].config({"background": "Blue"})
	listOfSlots[currentSlot].config({"foreground": "White"})

def rightPress(event):
	global currentSlot
	if currentSlot == 3:
		return
	listOfSlots[currentSlot].config({"background": "White"})
	listOfSlots[currentSlot].config({"foreground": "Black"})
	currentSlot += 1
	listOfSlots[currentSlot].config({"background": "Blue"})
	listOfSlots[currentSlot].config({"foreground": "White"})

def upPress(event):
	i = currentSlot
	while i < 3:
		listOfSlots[i].config({"text" : listOfSlots[i + 1].cget("text")})
		i += 1
	listOfSlots[3].config({"text" : "test"})


win.bind('<Left>', leftPress)
win.bind('<Right>', rightPress)
win.bind('<Up>', upPress)



win.mainloop()