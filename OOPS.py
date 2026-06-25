class Student:
    def __init__(self, fullname, RollNo):
        self.name = fullname
        print("adding new student in database..")
        self.rollno = RollNo
        print("Enter roll number")

s1 = Student("Karan", 23)
print(s1.name)
print(s1.rollno)
    
