## uoregon-cis422-p1

Shared repository for group: Cheetle®s CIS 422 Winter 2020 Project 1 at the University of Oregon

The goal of the project is for our group to successfully manage and develop a "Classroom Cold-Call Assist Software Program" largely based on the SRS written and provided by Professor Anthony Hornof.

## How to install:
1. Download the zip “G3ColdCall.zip”
2. Unzip the file “G3ColdCall.zip”
3. Double click ColdCall to open. NOTE: ColdCall and Cold_call_files must be in the same directory.
4. If ColdCall opens without error skip to step 8. If ColdCall does not open due to access rights you will have to change the access rights yourself.  Please continue to step 5.
5. Open Terminal and cd to the directory that ColdCall is in.
6. Type “chmod 777 ColdCall”
7. Open ColdCall again by double clicking
8. Click the “Import” button in the Cold Call window.
9. Find the class roster and open it. See  for the correct file formatting!
10. You are ready to use Cold Call for class!


## Correct File Formatting for Import
Note: This can also be found in cold_call_files -> docs -> technical -> File-Formatting.md.

The student roster needs to be a “.txt” file that is TAB-delimited, ideally generated by Excel. The first line of the file needs to contain the following (also TAB-delimited) header: “FirstName LastName ID-Number Email ColdCallCount Flag FlagCount”. The rows that follow should contain student information in the format according to the header above. Items are to be updated in place to reflect the current information after each action. The Python Standard Library's csv module contains all necessary functionality to simplify parsing and writing.
