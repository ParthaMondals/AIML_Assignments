import csv
from student import Student

def read_csv_record(filepath):
    student_list = []
    with open(filepath,"r") as file:
        rows = csv.reader(file)
        header = next(rows)
        for data in rows:
            if(data == ''):
                continue          
            s1 = Student(int(data[0]) , data[1] , data[2], int(data[3]),int(data[4]),int(data[5]),int(data[6]))
            student_list.append(s1)
    return student_list



def write_csv_record(filepath,record):
    with open(filepath,"w") as file:
        csv_writer = csv.writer(file)
        csv.wrier.writerows(record)
