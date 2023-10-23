class students:
    def __init__(self,name,course,gender,age):
        self.name=name
        self.course=course
        self.gender=gender
        self.age=age

    def wanafunzi(self):
        print("Name: %s \n Course: %s \n Gender %s \n Age: %d "
              % (self.name, self.course, self.gender, self.age))

stud1 = students("Eric Were", "Computer Science", "Male", 25)
stud2 = students("Irene Mungai","IST","Female", 20)
stud3 = students("Alexandria", "IBA", "Female", 26)
stud4 = students("Elvis","BioChemistry","Male", 30)

stud1.wanafunzi()
stud2.wanafunzi()
stud3.wanafunzi()
stud4.wanafunzi()


