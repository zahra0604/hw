students=[]

def add_student():
    name=input("enter student name")
    age=int(input("enter students age"))
    grade=float(input("Enter the students grade"))
    
    student={
        "name":name,
        "age":age,
        "grade":grade
    }
    students.append(student)
    print("Student added sucefully")
    

def show_student():
    if len(students)==0:
        print("no student found")
        return

    for student in students:
        print("name",student["name"])
        print("age",student["age"])
        print("grade",student["grade"])
        print("----------------------")
def delete_student():
    name=input("enter student name")
    for student in students:
        if student["name"].lower()==name.lower():
            
            students.remove(student)
            return
    print("student not found ")
        