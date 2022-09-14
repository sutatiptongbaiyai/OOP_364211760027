from EV_Car import EV_Car

#input data
def input_evcar_data():

    brand = input("Enter evcar brand: ")
    model = input("Enter evcar model: ")
    motor = input("Enter evcar motor: ")
    horsepower = input("Enter evcar horsepower: ")
    batterysize = input("Enter evcar batterysize: ")
    range = input("Enter evcar range: ")
    price = input("Enter evcar price: ")

    #return brand,model,motor,horsepower,batterysize,range,price # return as tuple
    my_evcar.append(vehicle(brand,model,motor,horsepower,batterysize,range,price))
    print("\n-----------------------------")
    print("เพิ่มข้อมูลเรียบร้อยแล้ว.")
    print("\n-----------------------------")

#display
def display_evcar():
    if len(my_evcar) == 0:
        print("คุณไม่ได้เพิ่มข้อมูล.")
    else:
        print(f'you had {len(my_evar)} following:')
        for x in my_evcar:
            x.evcar_detail()
    print("\n")

#option
def display_option_system():
    print("Welcome to EV_Car Data store System")
    print("1.เพิ่มข้อมูล EV_Car")
    print("2.แสดงข้อมูล EV_Car")
    print("3.ออกจากระบบ")
    select = int(input("เลือก (1-3)? :"))
    if select == 1:
        input_evcar_data()
    elif select == 2:
        display_evcar()
    elif select == 3:
        print("ขอบคุณค่ะ")
        exit(0)
    else:
        print("กรุณาเลือกหมายเลขบริการ 1-3.")

    my_evcar = []
    s = 0
    while s == 0:
        display_option_system()
