# Student Record Management System

## A. Title
Student Record Management System (SRMS)

## B. Objective
The objective of this assignment is to develop a command-line application in Python that demonstrates core concepts of Object-Oriented Programming (OOP) and file handling. The system maintains student academic profiles, performs computations on their grades, and stores/retrieves information using different file formats (plain TXT, structured CSV, and nested JSON).

## C. Features
Add a new student
Display student information (single or all)
Calculate total and average marks
Determine pass/fail result
Search for a student by ID
Update a student's marks
Remove a student
Read and write student data in TXT, CSV, and JSON formats
Command-line interface using argparse

## D. Project Structure

```text
student-record-system/
│
├── data/
│   ├── students_records.json
│   ├── student_data.txt
│   └── students_data.csv
│
├── file_handler/
│   ├── json_file_handler.py
│   ├── csv_file_handler.py
│   └── text_file_handler.py
│
├── main.py
├── student.py
└── student_manager.py
```

## E. Requirements
Python: Version 3.10 or higher (required for match-case statements in the CLI).
Dependencies: None. The system relies entirely on standard library modules (argparse, os, csv, json).

## F. How to Run
Run the program from the command line by providing the database file path and its format.

Run with Text file
```python main.py --file data/students.txt --format txt```
Run with CSV file
``` python main.py --file data/students.csv --format csv ```
Run with JSON file
``` python main.py --file data/students.json --format json ```

## Input and Output
Input: A TXT, CSV, or JSON file containing student records, given via --file and --format.
Files required: One of data/students.txt, data/students.csv, or data/students.json
Output: Student information printed to the console (ID, name, department, semester, marks, total, average, result). For add/update/remove actions, the updated records are also written back to a file.

## H. OOP Concepts Used
Classes: Used Student to model a single record and StudentManager to manage the collection of records.
Objects: Instances of Student are initialized dynamically from loaded file entries and user prompts.
Constructors: Defined __init__ in both classes to set up starting fields and initialize lists.
Instance Methods:
calculate_total() and calculate_average() process grade averages.
get_result() determines pass/fail thresholds (passing require ≥ 33 in every subject).
display_student() prints formatted terminal outputs.
add_student(), remove_student(), and search_student() manage memory state.

## I. File Handling Concepts Used
Context Managers (with open(...)): Ensures file streams are safely opened and closed without resource leaks.
CSV Parser (csv.reader & csv.writer): Reads and writes tabular data without relying on external libraries like Pandas.
JSON Serializer (json.load & json.dump): Loads structured tree data and writes formatted JSON using indent=4.
String Processing (strip(), split(), map()): Sanitizes spaces and splits text fields on commas when parsing raw .txt configurations.

## J. Sample Output
```text
PS E:\student record system> python main.py --file student_data.txt --format text
Enter 1 to add student

Enter 2 to remove a student

Enter 3 to search a student 

Enter 4 to calculate a student's total marks 

Enter 5 to calculate a student's average marks 

Enter 6 to display student information 

Enter 7 to save into a file
Enter 8 to exit
Enter here: 6
 sid - 101 ,Name -Rahul ,Department - Computer Science,Semester - 1, math - 78, physics = 82, chemistry = 69
 sid - 102 ,Name -Priya ,Department - Computer Science,Semester - 1, math - 91, physics = 87, chemistry = 94
 sid - 103 ,Name -Amit ,Department - Mathematics,Semester - 1, math - 65, physics = 71, chemistry = 68
 sid - 104 ,Name -Sneha ,Department - Physics,Semester - 2, math - 84, physics = 79, chemistry = 88
 sid - 105 ,Name -Arjun ,Department - Computer Science,Semester - 2, math - 73, physics = 76, chemistry = 81
 sid - 106 ,Name -Ananya ,Department - Mathematics,Semester - 2, math - 89, physics = 92, chemistry = 85
 sid - 107 ,Name -Rohan ,Department - Physics,Semester - 1, math - 62, physics = 68, chemistry = 74
 sid - 108 ,Name -Neha ,Department - Computer Science,Semester - 3, math - 95, physics = 90, chemistry = 93
 sid - 109 ,Name -Vikram ,Department - Mathematics,Semester - 3, math - 77, physics = 83, chemistry = 79
 sid - 110 ,Name -Ishita ,Department - Physics,Semester - 2, math - 86, physics = 81, chemistry = 90
Enter 1 to add student

Enter 2 to remove a student

Enter 3 to search a student 

Enter 4 to calculate a student's total marks 

Enter 5 to calculate a student's average marks 

Enter 6 to display student information 

Enter 7 to save into a file
Enter 8 to exit
Enter here: 3
Enter student id: 103
Yes student found
 sid - 103 ,Name -Amit ,Department - Mathematics,Semester - 1, math - 65, physics = 71, chemistry = 68
Enter 1 to add student

Enter 2 to remove a student

Enter 3 to search a student 

Enter 4 to calculate a student's total marks 

Enter 5 to calculate a student's average marks 

Enter 6 to display student information 

Enter 7 to save into a file
Enter 8 to exit
Enter here: 1
Enter student's details in single line: 112 anish statistics 2 69 89 75
Enter 1 to add student

Enter 2 to remove a student

Enter 3 to search a student 

Enter 4 to calculate a student's total marks 

Enter 5 to calculate a student's average marks 

Enter 6 to display student information 

Enter 7 to save into a file
Enter 8 to exit
Enter here: 2
Enter student id: 101
Enter 1 to add student

Enter 2 to remove a student

Enter 3 to search a student 

Enter 4 to calculate a student's total marks 

Enter 5 to calculate a student's average marks 

Enter 6 to display student information 

Enter 7 to save into a file
Enter 8 to exit
Enter here: 6
 sid - 102 ,Name -Priya ,Department - Computer Science,Semester - 1, math - 91, physics = 87, chemistry = 94
 sid - 103 ,Name -Amit ,Department - Mathematics,Semester - 1, math - 65, physics = 71, chemistry = 68
 sid - 104 ,Name -Sneha ,Department - Physics,Semester - 2, math - 84, physics = 79, chemistry = 88
 sid - 105 ,Name -Arjun ,Department - Computer Science,Semester - 2, math - 73, physics = 76, chemistry = 81
 sid - 106 ,Name -Ananya ,Department - Mathematics,Semester - 2, math - 89, physics = 92, chemistry = 85
 sid - 107 ,Name -Rohan ,Department - Physics,Semester - 1, math - 62, physics = 68, chemistry = 74
 sid - 108 ,Name -Neha ,Department - Computer Science,Semester - 3, math - 95, physics = 90, chemistry = 93
 sid - 109 ,Name -Vikram ,Department - Mathematics,Semester - 3, math - 77, physics = 83, chemistry = 79
 sid - 110 ,Name -Ishita ,Department - Physics,Semester - 2, math - 86, physics = 81, chemistry = 90
 sid - 112 ,Name -anish ,Department - statistics,Semester - 2, math - 69, physics = 89, chemistry = 75
Enter 1 to add student

Enter 2 to remove a student

Enter 3 to search a student 

Enter 4 to calculate a student's total marks 

Enter 5 to calculate a student's average marks 

Enter 6 to display student information 

Enter 7 to save into a file
Enter 8 to exit
Enter here: 8
Exiting from the program ...
```
## Learning Outcome / Conclusion
This assignment reinforced how to structure a small Python program using OOP — separating data (Student), collection management (StudentManager), and file I/O (file_handler.py) into distinct modules instead of one script. It also gave hands-on practice with Python's built-in csv and json modules alongside plain text file handling, and with building a command-line interface using argparse. The main difficulty was keeping the three file formats consistent with each other (same fields, same load/save behavior) while keeping each format's read/write logic isolated from the rest of the program.


