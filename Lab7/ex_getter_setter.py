"""
Name: {นางสาวสุธาทิพย์ ทองใบใหญ่}
SID: {364211760027}
Group: {MIT221}
"""

class Student:
    def __init__(self,name,id):
        # attributes
        self.__name = name # prvate  member
        self.__id = id # prvate member
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name

    def get_id(self):
        return self.__id

    def __str__(self):
        print(f'Name: {self.__name} ID: {self.__id}')


s = Student("Sam","001")
s.__str__()

print(s.get_name())
s.set_name("Nat")

print(s.get_name())

print(s.get_id())