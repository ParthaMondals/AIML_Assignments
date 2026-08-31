from student import Student
import json

def read_json_record(filepath):
    with open(filepath,"r") as file:
        data = json.load(file)
        student_list = []
        for i in data:
            s1 = Student(int(i['Student ID']), i['Name'], i['Department'], int(i['Semester']), int(i['Math']), int(i['Phy']), int(i['Chem']))
            student_list.append(s1)
    return student_list


def write_json_record(filepath, record):
    data = [
        {
            "Student ID": student.sid,
            "Name": student.name,
            "Department": student.Department,
            "Semester": student.Semester,
            "Math": student.Math,
            "Phy": student.Phy,
            "Chem": student.Chem
        }for student in record
    ]
    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)