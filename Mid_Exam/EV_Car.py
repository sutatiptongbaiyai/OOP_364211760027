"""
Name: {นางสาวสุธาทิพย์ ทองใบใหญ่}
SID: {364211760027}
Group: {MIT221}
"""

class EV_Car:
    my_evcar = []
    def __init__(self,brand,model,motor,horsepower,batterysize,range,price):
        self.brand = brand
        self.model = model
        self.motor = motor
        self.horsepower = horsepower
        self.batterysize = batterysize
        self.range = range
        self.price = price
        self.my_evcar.append(self)

    def EV_Car_detail(self):
            print(f'Brand:{self.brand} '
                  f'Model:{self.model} '
                  f'Motor:{self.motor} '
                  f'Horsepower:{self.horsepower} '
                  f'Batterysize:{self.batterysize} '
                  f'Range:{self.range} '
                  f'Price:{self.price} ')


