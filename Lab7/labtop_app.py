"""
Name: {นางสาวสุธาทิพย์ ทองใบใหญ่}
SID: {364211760027}
Group: {MIT221}
"""
from labtop import labtop

# display
def display_labtop():
    if len(my_labtop) ==0:
        print("You had no labtop data.")
    else:
        num = 1
        print(f'You had {len(my_labtop)} following:')
        for x in my_labtop:
            print(f'{num}. ',end="")
            x.display_labtop()
            num +=1
        print("\n")


# option
def display_option_system():
    select = 0
    print("Welcome to Loptop System")
    print("1.เพิ่มข้อมูล Laptop")
    print("2.แสดงข้อมูล Laptop")
    print("3.ลบข้อมูล Laptop")
    print("4.แก้ไขราคา")
    print("5.ออกจากระบบ")
    select = int(input("select(1-5)? : "))
    if select == 1:
        input_laptop_data()
    elif select == 2:
        display_labtop()
    elif select == 3:
        delete_labtop()
    elif select == 4:
        edit_labtop_price()
    elif select == 5:
        print("Good Bye.")
        exit(0)
    else:
        print("Please, select number 1-5.")


def edit_labtop_price():
    print("Which one do you want to edit price?: ")
    display_labtop()
    n = len(my_labtop)
    s = 1
    while s:
        s = int(input(f"select(1-{n}) or type 0 to main options:? "))
        if s in range(1, n + 1):
            print(f'old price: {my_labtop[s-1].get_Price()}')
            newprice = float(input("enter new price: "))
            my_labtop[s-1].set_Price(newprice)
            print("\nLaptop price updated.\n")
            break
        elif s == 0:
            break
        else:
            print(f"Please, select number 1-{n} or type 0 to main options.")


#delete data
def delete_labtop():
    print("Which one do you want to remove?: ")
    display_labtop()
    n = len(my_labtop)
    s = 1
    while s:
        s = int(input(f"select(1-{n}) or type 0 to main options:? "))
        if s in range(1,n+1):
            my_labtop.pop(s-1)
            print("\nAlready delete laptop data.\n")
            break
        elif s == 0:
            break
        else:
            print(f"Please, select number 1-{n} or type 0 to main options.")


# input data
def input_laptop_data():
    Brand = input("Enter laptop Brand: ")
    Model = input("Enter laptop Model: ")
    CPU = input("Enter laptop CPU: ")
    RAM = int(input("Enter laptop RAM(GB): "))
    Display = float(input("Enter laptop Display(inch): "))
    Storage = int(input("Enter laptop Storage(GB): "))
    Price = int(input("Enter laptop Price: "))

    l = labtop("","","",0,0,0,0)

    l.set_Brand(Brand)
    l.set_Model(Model)
    l.set_CPU(CPU)
    l.set_RAM(RAM)
    l.set_Display(Display)
    l.set_Storage(Storage)
    l.set_Price(Price)

   # my_labtop.append(labtop(Brand,Model,CPU,RAM,Display,Storage,Price))
    my_labtop.append(l)
    print("\n---------------------------------------------------")
    print("Already add loptop to store.")
    print("\n---------------------------------------------------")

my_labtop = []
my_labtop.append(labtop("ASUS","Vivobook15X","Intel Core i5-12500H",8,15.6,512,27990))
my_labtop.append(labtop("Lenovo","IdeaPadGaming3","Intel Core i5-11320H",8,15.6,512,25990))
my_labtop.append(labtop("Acer","Swifi 3","Intel Core i7-1260P",8,14,512,33990))
s = 0
while s == 0:
    display_option_system()