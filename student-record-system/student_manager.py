from csv_file_handler import *
from text_file_handler import *
from json_fil_handler import *
from student import Student

class studentmanager:
    def __init__(self):
        self.student_list = []
    
    def search_student(self,sid):
        for i in range(0,len(self.student_list)):
            if(self.student_list[i].sid == sid):
                return i
        print("Sorry, Student Not found")
        return 0

    def add_student(self,record_list):
        # Convert list to Student object: [sid, name, dept, sem, math, phy, chem]
        student = Student(int(record_list[0]), record_list[1], record_list[2], 
                         int(record_list[3]), int(record_list[4]), 
                         int(record_list[5]), int(record_list[6]))
        self.student_list.append(student)
        
    def remove_student(self,sid):
        for i in self.student_list:
            if(i.sid == sid):
                self.student_list.remove(i)

    def display_all_student(self):
        for i in range(0,len(self.student_list)):
            self.student_list[i].display()

    def load_from_file(self,filepath,filetype):
        if(filetype == "text"):
            self.student_list = read_student_record(filepath)
        elif(filetype == "csv"):
            self.student_list = read_csv_record(filepath)
        elif(filetype == "json"):
            self.student_list = read_json_record(filepath)
    
    def save_into_file(self,filepath,filetype):
            if(filetype == "text"):
                self.student_list = write_student_record(filepath,self.student_list)
            elif(filetype == "csv"):
                self.student_list = write_csv_record(filepath,self.student_list)
            elif(filetype == "json"):
                self.student_list = write_json_record(filepath,self.student_list)

