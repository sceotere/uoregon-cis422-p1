#File Formatting Instructions

This file details the rules for how student roster data, the session state, and log files are to be formatted. This writeup is a work in progress.

##Student Roster

The student roster shall be a `csv` (comma-separated values) file, with default path: `<default-roster-path>`

The first line of the file shall contain the following header:

`first name,last name,id number,email,cold-call count,flag,flag count`

The rows that follow shall contain student information in the format according to the header above.
Items are to be updated in place to reflect the current information after each action.

The Python Standard Library's csv module contains all necessary functionality to simplify parsing and writing.

##Session State
The session state shall be saved in two files in the same directory as the source code.
 
* `coldcall.ini` shall containing the following keys:

  ```
  rosterpath=<path to last opened roster csv file>
  deckindices=<comma separated indices of the students on deck, relevant to Roster.students>
  nextindex=<value of Roster.next indicating which index of the shuffled-order list we are grabbing a student from next>
  ```
 
* `order.conf` shall contain the entire contents of `Roster.order` in a single, comma-separated line of numbers.

##Log Files

_**TBD**_

We can decide on something that's easily readable output to a text file every action sounds good.

In the mean time, listen to either of these great songs:

* https://youtu.be/d0bJZGZ0s8U
* https://youtu.be/PN-zHSvDc1g