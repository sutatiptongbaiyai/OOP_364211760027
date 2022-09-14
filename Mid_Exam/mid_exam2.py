def display_EV_Car():
    if len(EV_Car) == 0:
        print("you had no EV_Car data.")
    else:
        print(f'you had {len(EV_Car)} following:')
        for x in EV_Car:
            x.EV_Car_detail()
    print("\n")