"""
Name: {นางสาวปนัดดา หลวงนา}
SID: {363411760007}
Group: {MIT421}
"""

class Student:
    #class attributes
    uni = "RUTS"
    my_std = []  # empty list

    def __init__(self,name,id,major):
        # object attributes
        self.name = name
        self.id = id
        self.major = major
        # add object to my_std (list)
        self.my_std.append(self)

    def introduce(self):
        print(f' MY name is {self.name},my id is {self.id}, and I am studying in {self.major} major.')

s1 = Student("Sutatip Tongbaiyai","111", "MIT221")
s1.introduce()

s2 = Student("Sutatip Tongbaiyai","222", "GG")
s2.introduce()

s1.major = "LM"
s1.introduce()

print(s1.uni)
print(s2.uni)

Student.uni = "PSU"
print(s1.uni)
print(s2.uni)

print(len(Student.my_std))

print(Student.my_std[0].introduce)
