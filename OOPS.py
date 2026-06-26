class Student:
    college_name = "ABC College"

    def __init__(self, fullname, RollNo):
        self.name = fullname
        print("adding new student in database..")
        self.RollNo = RollNo
        print("Enter roll number")

    def welcome(self):
        print("Welcome student", self.name)
    def get_RollNo(self):
        return self.RollNo

s1 = Student("Karan", 23)
print(s1.name)
print(s1.RollNo)
s1.welcome()
s1.get_RollNo()

    
