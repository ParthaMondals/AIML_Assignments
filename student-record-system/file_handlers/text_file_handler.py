from student import Student

filepath = "student_data.txt"

def read_student_record(filepath):
    with open(filepath,"r") as file:
        content = file.readlines()

        student_list = []

        for i in range(1,len(content)):
             if(content[i].strip() == ''):
                 continue
            
             data = content[i].strip().split(",")
             s1 = Student(int(data[0]) , data[1] , data[2], int(data[3]),int(data[4]),int(data[5]),int(data[6]))
             student_list.append(s1)
             
        return student_list

def write_student_record(filepath,record):
    with open(filepath,"w") as file:
        file.write(record)
