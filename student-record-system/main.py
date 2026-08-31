import argparse
from student_manager import studentmanager

parser = argparse.ArgumentParser(description="Student Record Management System")
parser.add_argument("--file", required=True, help="input file path")
parser.add_argument(
    "--format", required=True, choices=["text", "csv", "json"], help="file format"
    )
args = parser.parse_args()

manager = studentmanager()
manager.load_from_file(args.file, args.format)

while True:
    print("Enter 1 to add student\n")
    print("Enter 2 to remove a student\n")
    print("Enter 3 to search a student \n")
    print("Enter 4 to calculate a student's total marks \n")
    print("Enter 5 to calculate a student's average marks \n")
    print("Enter 6 to display student information \n")
    print("Enter 7 to save into a file")
    print("Enter 8 to exit")

    n = int(input("Enter here: "))
    match n:
        case 1:
            q = input("Enter student's details in single line: ")
            l = q.split()
            manager.add_student(l)
        case 2:
            s = int(input("Enter student id: "))
            manager.remove_student(s)
        case 3:
            s = int(input("Enter student id: "))
            if(manager.search_student(s)):
                print("Yes student found")
                manager.student_list[manager.search_student(s)].display()
        case 4:
            s = int(input("Enter student id: "))
            if(manager.search_student(s)):
                manager.student_list[manager.search_student(s)].total()
        case 5:
            s = int(input("Enter student id: "))
            if(manager.search_student(s)):
                manager.student_list[manager.search_student(s)].average()
        case 6 :
            manager.display_all_student() 
        case 7:
            manager.save_into_file()     
        case 8:
            print("Exiting from the program ... ")
            break
        case _:
            print("Invalid input, please try again")
        
