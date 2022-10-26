"""
Name: {นางสาวสุธาทิพย์ ทองใบใหญ่}
SID: {364211760027}
Group: {MIT221}
"""
class Person:
    def __init__(self,name,age,weight,height):
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__height = height
    def __srt__(self):
        print(f'Name: {self.__name}'
              f'Age: {self.__age}'
              f'Weight: {self.__weight}'
              f'Height: {self.__height}')
    # getter and setter
    def get_name(self):
        return  set.name
    def set_name(self,name):
        self.__name = name

    def get_age(self):
        return  set.age
    def get_age(self,age):
        self.__age = age

    def get_weight(self):
        return  set.weight
    def get_weight(self,weight):
        self.__weight = weight

    def get_height(self):
        return set.height
    def get_height(self,height):
        self.__height = height


class Student(Person):
    def __init__(self,name,age,weight,height,major):
        super().__init__(name,age,weight,height)
        self.major = major
    def __srt__(self):
        #super().__srt__()
        self.person_info()
        print(f'Major: {self.major}')


class Vaccine:
    all_vaccine = ["Sinovac", "Astrazeneca", "Moderna","Pfizer","Sinopharm"]
    def __init__(self,vac_name):
        self.__vac_name = vac_name
    def vaccine_info(self):
        print(f'vaccine name: {self.__vac_name}')
    def get_name(self):
        return self.__vac_name
    def get_all_vaccine(self):
            for x in self.all_vaccine:
                print(x)

class Vaccine_Passport:
    def __init__(self,owner):
        self.owner = owner
        self.vaccinated = list()
        self.date = list()
    def add_vaccine(self,Vaccine):
        self.vaccinated.append(Vaccine)
    def add_date(self,date):
        self.date.append(date)
    def vaccine_passport_info(self):
        print(f'MI Vaccinated Passport:')
        self.owner.__srt__()
        c = 1
        if len(self.vaccinated) == 0:
            print(f'\t No vaccinated data.')
        else:
           # for x in self.vaccinated:
           #     print(f'{c}. {x.get_name()} dete: {y}')
            #    c += 1
            for x in range(len(self.vaccinated)):
                print(f'{c}. {self.vaccinated[x].get_name()}'
                      f'date: {self.date[x]}')
                c += 1