class People:

    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex


class Student(People):
    # def __init__(self,name,age,sex,school):
    #     People.__init__(self,name,age,sex)
    #     self.__school = school

    # def printproperty(self):
    #     print(self.name,self.age,self.sex,self.__school)
    def printproperty(self):
        print(self.name,self.age,self.sex)


# student = Student('lqf',26,'man','sz')
student = Student('lqf',26,'man')

student.printproperty()