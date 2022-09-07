from vehicle import vehicle


#display
def display_vehicle():
    if len(my_vehicle) == 0:
        print("you had no vehicle data.")
    else:
        print(f'you had {len(my_vehicle)} following:')
        for x in my_vehicle:
            x.vehicle_detail()
    print("\n")

#option
def display_option():
    print("Welcome to Vehicle Data store System (VDSS)")
    print("1.Add Vehicle")
    print("2.Display all Vehicle")
    print("3.exit")
    select = int(input("select (1-3)? :"))
    if select == 1:
        input_vehicle_data()
    elif select == 2:
        display_vehicle()
    elif select == 3:
        print("Good Bye")
        exit(0)
    else:
        print("Please, select number 1-3.")


#input data
def input_vehicle_data():

    brand = input("Enter vehicle brand: ")
    model = input("Enter vehicle model: ")
    color = input("Enter vehicle color: ")
    maxspeed = input("Enter vehicle maxspeed: ")
    price = input("Enter vehicle price: ")

    #return brand,model,color,maxspeed,price # return as tuple
    my_vehicle.append(vehicle(brand,model,color,maxspeed,price))
    print("\n-----------------------------")
    print("Already add vehicle to stoes.")
    print("\n-----------------------------")


my_vehicle = []
s = 0
while s == 0:
    display_option()


#vm = input_vehicle_data()
#print(type(vm))
#v1 = vehicle(vm[0], vm[1], vm[2], vm[3], vm[4])
#v1.vehicle_detail()

#vm = input_vehicle_data()
#print(vm)
#print(type(vm))
#v2 = vehicle(vm[0], vm[1], vm[2], vm[3], vm[4])
#v2.vehicle_detail()