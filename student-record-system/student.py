
class Student:
    def __init__(self,sid,name,dept,sem,math,phy,chem):
        self.sid = sid
        self.name = name
        self.dept = dept
        self.sem = sem
        self.math = math
        self.phy = phy
        self.chem = chem

    def display(self):
        print(f" sid - {self.sid} ,Name -{self.name} ,Department - {self.dept},Semester - {self.sem}, math - {self.math}, physics = {self.phy}, chemistry = {self.chem}")

    def total(self):
        print(f"Total marks by {self.name} is {self.math + self.phy + self.chem}")

    def average(self):
        print(f"Total marks by {self.name} is {round((self.math + self.phy + self.chem)/3,3)}")
    
    def get_result(self):
        print(f"Name:{self.name} Math: {self.math} Physics:{self.phy} ,  chemistry: {self.chem}")



    
    
