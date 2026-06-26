class Student:

    def __init__ (self, name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
    
    def avg(self):
        sum = self.mark1+self.mark2+self.mark3
        print("Hi",self.name,"your avg score is:", sum/3)

s1=Student("Vidya", 12,23,45)
s1.avg()
