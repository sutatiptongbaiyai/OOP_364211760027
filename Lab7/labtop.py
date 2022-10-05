"""
Name: {นางสาวสุธาทิพย์ ทองใบใหญ่}
SID: {364211760027}
Group: {MIT221}
"""
class labtop:
    #class attribute
    my_labtop = []

    def __init__(self,Brand,Model,CPU,RAM,Display,Storage,Price):
        self.__Brand = Brand
        self.__Model = Model
        self.__CPU = CPU
        self.__RAM = RAM
        self.__Display = Display
        self.__Storage = Storage
        self.__Price = Price
        self.my_labtop.append(self)

    def display_labtop(self):
        print(f'Brand:{self.__Brand} '
              f'Model:{self.__Model} '
              f'CPU:{self.__CPU} '
              f'RAM:{self.__RAM}'
              f'Display:{self.__Display} '
              f'Storage:{self.__Storage} '
              f'Price:{self.__Price}')

    def get_Brand(self):
        return self.__Brand

    def set_Brand(self, __Brand):
        self.__Brand = __Brand

    def get_Model(self):
        return self.__Model

    def set_Model(self, __Model):
        self.__Model = __Model

    def get_CPU(self):
        return self.__CPU

    def set_CPU(self, __CPU):
        self.__CPU = __CPU

    def get_RAM(self):
        return self.__RAM

    def set_RAM(self, __RAM):
        self.__RAM = __RAM

    def get_Display(self):
        return self.__Display

    def set_Display(self, __Display):
        self.__Display = __Display

    def get_Storage(self):
        return self.__Storage

    def set_Storage(self, __Storage):
        self.__Storage = __Storage

    def get_Price(self):
        return self.__Price

    def set_Price(self, __Price):
        self.__Price = __Price
