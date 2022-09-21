"""
Name: {นางสาวสุธาทิพย์ ทองใบใหญ่}
SID: {364211760027}
Group: {MIT221}
"""

class Person:
    def __init__(self,name,age):
        self._name = name
        self._age = age
    def __str__(self):
        print(f'Name: {self._name} Age: {self._age} ')

class Student(Person):
    def __init__(self,name,age,major):
        self.major = major
        Person.__init__(self,name,age)
    def __str__(self):
        print(f'Name: {self._name} Age: {self._age} Major: {self.major}')

p = Person("Puriwet",35)
p.__str__()

p._name = "Nattapong"
p.__str__()

s = Student("piyapong",37,"MIT")
s.__str__()

s._name = "pornprasert"
s.__str__()
