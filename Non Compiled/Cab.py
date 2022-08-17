import pickle
import os

try:
    Car_AC = pickle.load(open('data/CarAC.dat', 'rb'))
    Car_NonAC = pickle.load(open('data/Car_NonAC.dat', 'rb'))
    Van_AC = pickle.load(open('data/Van_AC.dat', 'rb'))
    Van_NonAC = pickle.load(open('data/Van_NonAC.dat', 'rb'))
    _3Wheel = pickle.load(open('data/_3Wheel.dat', 'rb'))
    Truck_7ft = pickle.load(open('data/Truck_7ft.dat', 'rb'))
    Truck_12ft = pickle.load(open('data/Truck_12ft.dat', 'rb'))
    Lorry_2500 = pickle.load(open('data/Lorry_2500.dat', 'rb'))
    Lorry_3500 = pickle.load(open('data/Lorry_3500.dat', 'rb'))

    Reserved_Car_AC = pickle.load(open('data/Reserved_Car_AC.dat', 'rb'))
    Reserved_Car_NonAC = pickle.load(open('data/Reserved_Car_NonAC.dat', 'rb'))
    Reserved_Van_AC = pickle.load(open('data/Reserved_Van_AC.dat', 'rb'))
    Reserved_Van_NonAC = pickle.load(open('data/Reserved_Van_NonAC.dat', 'rb'))
    Reserved_3Wheel = pickle.load(open('data/Reserved_3Wheel.dat', 'rb'))
    Reserved_Truck_7ft = pickle.load(open('data/Reserved_Truck_7ft.dat', 'rb'))
    Reserved_Truck_12ft = pickle.load(open('data/Reserved_Truck_12ft.dat', 'rb'))
    Reserved_Lorry_2500 = pickle.load(open('data/Reserved_Lorry_2500.dat', 'rb'))
    Reserved_Lorry_3500 = pickle.load(open('data/Reserved_Lorry_3500.dat', 'rb'))

except:
    print('Unable to Load Data files. Program will terminated')
    exit()

def add_vehicle():
    print('\nVehicle Categories : \n1 - Car \n2 - Van\n3 - 3 Wheelers\n4 - Truck\n5 - Lorry\n')
    Category = input('Select Category : ')

    try:
        _Category = int(Category)

    except:
        print('Invalid input. input must be a numeric value between 1 to 5')

    if _Category == 1:
        print('Selected Category : CAR')
        number = input('Enter Number - plate of Vehicle : ')
        if number == '':
            print('Number-plate is required !')
        else:
            AC = input('Does your Car has AC :\n1.YES \n2.NO \nEnter your choice : ')

            if AC == '1':
                if number in Car_AC:
                    print('This number-plate is already existing')
                else:
                    Car_AC.insert(0, number)
                    print('Your CAR has been successfully Added.\n')
            else:
                if number in Car_NonAC:
                    print('This number-plate is already existing')
                else:
                    Car_NonAC.insert(0, number)
                    print('Your CAR has been successfully Added.\n')

    elif _Category == 2:
        print('Selected Category : VAN')
        number = input('Enter Number - plate of Vehicle : ')
        if number == '':
            print('Number-plate is required !')
        else:
            AC = input('Does your Van has AC :\n1.YES \n2.NO \nEnter your choice : ')

            if AC == '1':
                if number in Van_AC:
                    print('This number-plate is already existing')

                else:
                    Van_AC.insert(0, number)
                    print('Your VAN has been successfully Added.\n')
            else:
                if number in Van_NonAC:
                    print('This number-plate is already existing')
                else:
                    Van_NonAC.insert(0, number)
                    print('Your VAN has been successfully Added.\n')


    elif _Category == 3:
        print('Selected Category : 3 Wheeler')

        number = input('Enter Number - plate of Vehicle : ')
        if number == '':
            print('Number-plate is required !')
        else:
            if number in _3Wheel:
                print('This number-plate is already existing')
            else:
                _3Wheel.insert(0, number)
                print('Your 3 Wheeler has been successfully Added.\n')

    elif _Category == 4:
        print('Selected Category : Truck')
        number = input('Enter Number - plate of Vehicle : ')
        if number == '':
            print('Number-plate is required !')
        else:
            Size = input('Size of Truck : \n1 - 7ft \n2 - 12ft \nEnter your choice : ')
    
            if Size == '1':
                if number in Truck_7ft:
                    print('This number-plate is already existing')
                else:
                    Truck_7ft.insert(0, number)
                    print('Your Truck has been successfully Added.\n')
    
            elif Size == '2':
                if number in Truck_12ft:
                    print('This number-plate is already existing')
                else:
                    Truck_12ft.insert(0, number)
                    print('Your Truck has been successfully Added.\n')
            else:
                print('Invalid Input. input must be 1 or 2')


    elif _Category == 5:
        print('Selected Category : Lorry')

        number = input('Enter Number - plate of Vehicle : ')
        if number == '':
            print('Number-plate is required !')
        else:
            maxWeight = input('Size of Lorry :\n1 - 2500KG \n2 - 3500KG \nEnter your choice : ')
    
            if maxWeight == '1':
                if number in Lorry_2500:
                    print('This number-plate is already existing')
                else:
                    Lorry_2500.insert(0, number)
                    print('Your Lorry has been successfully Added.\n')
    
            elif maxWeight == '2':
                if number in Lorry_3500:
                    print('This number-plate is already existing')
                else:
                    Lorry_3500.insert(0, number)
                    print('Your Lorry has been successfully Added.\n')
    
            else:
                print('Invalid Input. input must be 1 or 2')
           
    else:
        print('Input must be between 1 to 5')


def remove_vehicle():
    noVehicle = False
    noVehicle1 = False

    print('\nVehicle Categories : \n1 - Car \n2 - Van\n3 - 3 Wheelers\n4 - Truck\n5 - Lorry\n')
    Category = input('Enter Category : ')

    try:
        _Category = int(Category)

        if _Category == 1:
            if len(Car_AC) != 0:

                print('\nVehicles in CAR - AC :')
                for num in Car_AC:
                    print(num)

            else:
                print('\nNo vehicles in Car - AC')
                noVehicle = True

            if len(Car_NonAC) != 0:
                noVehicle = False
                print('\nCAR - NonAC :')
                for num in Car_NonAC:
                    print(num)
            else:
                print('\nNo vehicles in Car - NonAC')
                noVehicle1 = True

            if noVehicle == False or noVehicle1 == False:

                _remove = input('Enter a Number-plate to remove: ')

                if _remove in Car_AC:
                    Car_AC.remove(_remove)
                    print('Vehicle Removed')

                elif _remove in Car_NonAC:
                    Car_NonAC.remove(_remove)
                    print('Vehicle Removed')

                else:
                    print('Entered Number-plate is Invalid or Not existing')

            else:
                print('No Vehicles in This Category')


        elif _Category == 2:
            if len(Van_AC) != 0:
                print('\nVehicles in Van - AC :')
                for num in Van_AC:
                    print(num)
            else:
                print('\nNo vehicles in Van - AC')
                noVehicle = True

            if len(Van_NonAC) != 0:
                noVehicle = False
                print('\nVan - NonAC :')
                for num in Van_NonAC:
                    print(num)
            else:
                print('\nNo vehicles in Van - NonAC')
                noVehicle1 = True

            if noVehicle == False or noVehicle1 == False:

                _remove = input('Enter a Number-plate to remove: ')

                if _remove in Van_AC:
                    Van_AC.remove(_remove)
                    print('Vehicle Removed')

                elif _remove in Van_NonAC:
                    Van_NonAC.remove(_remove)
                    print('Vehicle Removed')

                else:
                    print('Entered Number-plate is Invalid or Not existing')

            else:
                print('No Vehicles in This Category')

        elif _Category == 3:
            if len(_3Wheel) != 0:
                print('\nVehicles in 3 Wheelers :')
                for num in Van_AC:
                    print(num)
            else:
                print('\nNo vehicles in 3 Wheelers')
                noVehicle = True

            if noVehicle == False:

                _remove = input('Enter a Number-plate to remove: ')

                if _remove in _3Wheel:
                    _3Wheel.remove(_remove)
                    print('Vehicle Removed')

                else:
                    print('Entered Number-plate is Invalid or Not existing')

        elif _Category == 4:
            if len(Truck_7ft) != 0:
                print('\nVehicles in Truck - 7ft :')
                for num in Truck_7ft:
                    print(num)
            else:
                print('\nNo vehicles in Truck - 7ft')
                noVehicle = True

            if len(Truck_12ft) != 0:
                noVehicle = False
                print('\nTruck - 12ft :')
                for num in Truck_12ft:
                    print(num)
            else:
                print('\nNo vehicles in Truck - 12ft')
                noVehicle1 = True

            if noVehicle == False or noVehicle1 == False:

                _remove = input('Enter a Number-plate to remove: ')

                if _remove in Truck_7ft:
                    Truck_7ft.remove(_remove)
                    print('Vehicle Removed')

                elif _remove in Truck_12ft:
                    Truck_12ft.remove(_remove)
                    print('Vehicle Removed')

                else:
                    print('Entered Number-plate is Invalid or Not existing')
            else:
                print('No Vehicles in This Category')

        elif _Category == 5:
            if len(Lorry_2500) != 0:
                print('\nVehicles in Lorry - 2500KG :')
                for num in Lorry_2500:
                    print(num)
            else:
                print('\nNo vehicles in Lorry - 2500KG')
                noVehicle = True

            if len(Lorry_3500) != 0:
                noVehicle = False
                print('\nLorry - 3500KG :')
                for num in Lorry_3500:
                    print(num)
            else:
                print('\nNo vehicles in Lorry - 3500KG')
                noVehicle1 = True

            if noVehicle == False or noVehicle1 == False:

                _remove = input('Enter a Number-plate to remove: ')

                if _remove in Lorry_2500:
                    Lorry_2500.remove(_remove)
                    print('Vehicle Removed')

                elif _remove in Lorry_3500:
                    Lorry_3500.remove(_remove)
                    print('Vehicle Removed')

                else:
                    print('Entered Number-plate is Invalid or Not existing')

        else:
            print('Input must be between 1 to 5')

    except:
        print('Input must be numeric')


def reserve():
    Q1 = input('What is your purpose ? \n1. Transport Passenger \n2. Transport Goods \nEnter Your Choice : ')

    if Q1 == '1':
        Q2 = input('How many Passengers (1 - 8): ')
        Q3 = input('Do you need AC ? \n1.YES \n2.N0 \nEnter your choice : ')

        try:
            _Q2 = int(Q2)

            if 8 >= _Q2 > 4 and Q3 == '1':
                print('Your Requirements match with VAN with AC\n')
                if len(Van_AC) == 0:
                    print('Sorry! Currently AC - Vans are not available in the system')
                else:
                    Q4 = input('Do you want to Hire Van with AC ? :\n1. YES\n2. NO\nEnter Your Choice : ')
                    if Q4 == '1':
                        nic = input('Enter Customer NIC :')

                        if nic == '':
                            print('NIC is Required!')

                        else:
                            if nic in Reserved_Van_AC.keys():
                                print('Already Reserved a Vehicle for this NIC')

                            else:
                                temp_vehicle = Van_AC[-1]
                                Reserved_Van_AC[nic] = temp_vehicle
                                Van_AC.remove(temp_vehicle)
                                print('----- Reservation Details -----')
                                print('NIC : ', nic)
                                print('Vehicle No : ', temp_vehicle)
                                print('Vehicle Successfully Reserved')

                    elif Q4 == '2':
                        print('Reservation Cancelled.\nYou will be redirected to Home Screen')

                    else:
                        print('Invalid input. Expected input is 1 or 2')

            elif 8 >= _Q2 > 4 and Q3 == '2':
                print('Your Requirements match with VAN without AC\n')
                if len(Van_NonAC) == 0:
                    print('Sorry! Currently NonAC - Vans are not available in the system')
                else:
                    Q4 = input('Do you want to Hire Van without AC ? :\n1. YES\n2. NO\nEnter Your Choice : ')
                    if Q4 == '1':
                        nic = input('Enter Customer NIC :')

                        if nic == '':
                            print('NIC is Required!')

                        else:
                            if nic in Reserved_Van_NonAC.keys():
                                print('Already Reserved a Vehicle for this NIC')

                            else:
                                temp_vehicle = Van_NonAC[-1]
                                Reserved_Van_NonAC[nic] = temp_vehicle
                                Van_NonAC.remove(temp_vehicle)
                                print('----- Reservation Details -----')
                                print('NIC : ', nic)
                                print('Vehicle No : ', temp_vehicle)
                                print('Vehicle Successfully Reserved')

                    elif Q4 == '2':
                        print('Reservation Cancelled.\nYou will be redirected to Home Screen')

                    else:
                        print('Invalid input. Expected input is 1 or 2')


            elif 4 >= _Q2 > 0 and Q3 == '1':
                print('Your Requirements match with CAR with AC\n')
                if len(Car_AC) == 0:
                    print('Sorry! Currently AC - Cars are not available in the system')
                else:
                    Q4 = input('Do you want to Hire CAR with AC ? :\n1. YES\n2. NO\nEnter Your Choice : ')
                    if Q4 == '1':
                        nic = input('Enter Customer NIC :')

                        if nic == '':
                            print('NIC is Required!')

                        else:
                            if nic in Reserved_Car_AC.keys():
                                print('Already Reserved a Vehicle for this NIC')

                            else:
                                temp_vehicle = Car_AC[-1]
                                Reserved_Car_AC[nic] = temp_vehicle
                                Car_AC.remove(temp_vehicle)
                                print('----- Reservation Details -----')
                                print('NIC : ', nic)
                                print('Vehicle No : ', temp_vehicle)
                                print('Vehicle Successfully Reserved')

                    elif Q4 == '2':
                        print('Reservation Cancelled.\nYou will be redirected to Home Screen')

                    else:
                        print('Invalid input. Expected input is 1 or 2')

            elif 4 >= _Q2 > 0 and Q3 == '2':
                if _Q2 in range(1, 4):
                    print('Your Requirements match with Non-AC CAR or 3 Wheeler\n')
                    if len(Car_NonAC) != 0 and len(_3Wheel) != 0:
                        Q4 = input('Do you want to hire NonAC CAR or 3 Wheeler ? :\n1. NonAC Car \n2. 3-Wheeler \n3. Exit \nEnter Your Choice : ')
                        if Q4 == '1':
                            nic = input('Enter Customer NIC :')

                            if nic == '':
                                print('NIC is Required!')

                            else:
                                if nic in Reserved_Car_NonAC.keys():
                                    print('Already Reserved a Vehicle for this NIC')

                                else:
                                    temp_vehicle = Car_NonAC[-1]
                                    Reserved_Car_NonAC[nic] = temp_vehicle
                                    Car_NonAC.remove(temp_vehicle)
                                    print('----- Reservation Details -----')
                                    print('NIC : ', nic)
                                    print('Vehicle No : ', temp_vehicle)
                                    print('Vehicle Successfully Reserved')

                        elif Q4 == '2':
                            nic = input('Enter Customer NIC :')

                            if nic == '':
                                print('NIC is Required!')

                            else:
                                if nic in Reserved_3Wheel.keys():
                                    print('Already Reserved a Vehicle for this NIC')

                                else:
                                    temp_vehicle = _3Wheel[-1]
                                    Reserved_3Wheel[nic] = temp_vehicle
                                    _3Wheel.remove(temp_vehicle)
                                    print('----- Reservation Details -----')
                                    print('NIC : ', nic)
                                    print('Vehicle No : ', temp_vehicle)
                                    print('Vehicle Successfully Reserved')

                        elif Q4 == '3':
                            print('Reservation Cancelled.\nYou will be redirected to Home Screen')

                        else:
                            print('Invalid input. Expected input is 1,2 or 3.')

                    elif len(Car_NonAC) == 0:
                        if len(_3Wheel) == 0:
                            print('Sorry! NonAC - Car and 3 Wheelers not available in the system')
                        else:
                            print('Sorry! NonAC - Car not available in the system')
                            Q4 = input('Do you want to Hire  3 Wheeler ? :\n1. Yes \n2. No \nEnter Your Choice : ')

                            if Q4 == '1':
                                nic = input('Enter Customer NIC :')

                                if nic == '':
                                    print('NIC is Required!')

                                else:
                                    if nic in Reserved_3Wheel.keys():
                                        print('Already Reserved a Vehicle for this NIC')

                                    else:
                                        temp_vehicle = _3Wheel[-1]
                                        Reserved_3Wheel[nic] = temp_vehicle
                                        _3Wheel.remove(temp_vehicle)
                                        print('----- Reservation Details -----')
                                        print('NIC : ', nic)
                                        print('Vehicle No : ', temp_vehicle)
                                        print('Vehicle Successfully Reserved')

                            elif Q4 == '2':
                                print('Reservation Cancelled.\nYou will be redirected to Home Screen')

                            else:
                                print('Invalid input. Expected input is 1 or 2.')

                    elif len(_3Wheel) == 0:
                        if len(Car_NonAC) == 0:
                            print('Sorry! NonAC - Car and 3 Wheelers not available in the system')
                        else:
                            print('Sorry! 3 Wheelers not available in the system')
                            Q4 = input('Do you want to Hire NonAC - Car ? :\n1. Yes \n2. No \nEnter Your Choice : ')

                            if Q4 == '1':
                                nic = input('Enter Customer NIC :')

                                if nic == '':
                                    print('NIC is Required!')

                                else:
                                    if nic in Reserved_Car_NonAC.keys():
                                        print('Already Reserved a Vehicle for this NIC')

                                    else:
                                        temp_vehicle = Car_NonAC[-1]
                                        Reserved_Car_NonAC[nic] = temp_vehicle
                                        Car_NonAC.remove(temp_vehicle)
                                        print('----- Reservation Details -----')
                                        print('NIC : ', nic)
                                        print('Vehicle No : ', temp_vehicle)
                                        print('Vehicle Successfully Reserved')

                            elif Q4 == '2':
                                print('Reservation Cancelled.\nYou will be redirected to Home Screen')

                    else:
                        print('Invalid input. Expected input is 1,2 or 3.')

            else:
                print("You don't have a choice")

        except:
            print('Check you input for number of passenger')


    elif Q1 == '2':
        Q2 = input('\n1. Truck ( 7ft / 12ft) \n2. Lorry ( 2500KG / 3500KG) \nEnter Your Choice : ')

        if Q2 == '1':
                print('Truck Selected \nChoose Truck Size :')
                Q3 = input('1. 7ft  \n2. 12ft \nEnter Your Choice : ')
                if Q3 == '1':
                    if len(Truck_7ft) != 0:
                        nic = input('Enter Customer NIC :')

                        if nic == '':
                            print('NIC is Required!')

                        else:
                            if nic in Reserved_Truck_7ft.keys():
                                print('Already Reserved a Vehicle for this NIC')

                            else:
                                temp_vehicle = Truck_7ft[-1]
                                Reserved_Truck_7ft[nic] = temp_vehicle
                                Truck_7ft.remove(temp_vehicle)
                                print('----- Reservation Details -----')
                                print('NIC : ', nic)
                                print('Vehicle No : ', temp_vehicle)
                                print('Vehicle Successfully Reserved')
                    else:
                        print('Sorry! Currently 7ft Trucks are not available in the system')

                elif Q3 == '2':
                    if len(Truck_12ft) != 0:
                        nic = input('Enter Customer NIC :')

                        if nic == '':
                            print('NIC is Required!')

                        else:
                            if nic in Reserved_Truck_12ft.keys():
                                print('Already Reserved a Vehicle for this NIC')

                            else:
                                temp_vehicle = Truck_12ft[-1]
                                Reserved_Truck_12ft[nic] = temp_vehicle
                                Truck_12ft.remove(temp_vehicle)
                                print('----- Reservation Details -----')
                                print('NIC : ', nic)
                                print('Vehicle No : ', temp_vehicle)
                                print('Vehicle Successfully Reserved')

                    else:
                        print('Sorry! Currently 12ft Trucks are not available in the system')

        elif Q2 == '2':
            print('Lorry Selected\n')
            Q3 = input('1. 2500KG \n2. 3500KG \nEnter Your Choice : ')
            if Q3 == '1':
                if len(Lorry_2500) != 0:
                    nic = input('Enter Customer NIC :')

                    if nic == '':
                        print('NIC is Required!')

                    else:
                        if nic in Reserved_Lorry_2500.keys():
                            print('Already Reserved a Vehicle for this NIC')

                        else:
                            temp_vehicle = Lorry_2500[-1]
                            Reserved_Lorry_2500[nic] = temp_vehicle
                            Lorry_2500.remove(temp_vehicle)
                            print('----- Reservation Details -----')
                            print('NIC : ', nic)
                            print('Vehicle No : ', temp_vehicle)
                            print('Vehicle Successfully Reserved')

                else:
                    print('Sorry! Currently Lorry 2500KG are not available in the system')


            elif Q3 == '2':
                if len(Lorry_3500) != 0:
                    nic = input('Enter Customer NIC :')

                    if nic == '':
                        print('NIC is Required!')

                    else:
                        if nic in Reserved_Lorry_3500.keys():
                            print('Already Reserved a Vehicle for this NIC')

                        else:
                            temp_vehicle = Lorry_3500[-1]
                            Reserved_Lorry_3500[nic] = temp_vehicle
                            Lorry_3500.remove(temp_vehicle)
                            print('----- Reservation Details -----')
                            print('NIC : ', nic)
                            print('Vehicle No : ', temp_vehicle)
                            print('Vehicle Successfully Reserved')

                else:
                    print('Sorry! Currently Lorry 3500KG are not available in the system')

            else:
                print('Invalid input. Expected input 1 or 2.')


        else:
            print('Invalid input. Expected input 1 or 2.')


def release():
    print('Vehicle Categories : \n1 - Car \n2 - Van\n3 - 3 Wheelers\n4 - Truck\n5 - Lorry\n')
    Category = input('Enter Category : ')

    if Category == "1":

        subcategory = input('1. AC - Car \n2. NonAC - Car \nEnter your Choice :')

        if subcategory == '1':

            nic = input('Enter Customer NIC :')

            if nic in Reserved_Car_AC.keys():
                print(nic, ' Hired ', Reserved_Car_AC[nic])

                RemoveRq = input('Do You want to Release This vehicle ? \n1. Yes \n2. NO \nEnter your choice : ')

                if RemoveRq == '1':
                    temp = Reserved_Car_AC[nic]
                    Car_AC.insert(0, temp)
                    Reserved_Car_AC.pop(nic)
                    print(temp, 'is Successfully Released')

                if RemoveRq == '2':
                    print('Task Canceled. You will be redirected to Home menu')

            else:
                print('No AC - Car Reserved for this NIC')


        elif subcategory == "2":

            nic = input('Enter Customer NIC :')

            if nic in Reserved_Car_NonAC.keys():
                print(nic, ' Hired ', Reserved_Car_NonAC[nic])

                RemoveRq = input('Do You want to Release This vehicle ? \n1. Yes \n2. NO \nEnter your choice : ')

                if RemoveRq == '1':
                    temp = Reserved_Car_NonAC[nic]
                    Car_NonAC.insert(0, temp)
                    Reserved_Car_NonAC.pop(nic)
                    print(temp, 'is Successfully Released')

                if RemoveRq == '2':
                    print('Task Canceled. You will be redirected to Home menu')

            else:
                print('No NonAC - Car Reserved for this NIC')

        else:
            print('Invalid input. input must be 1 or 2.')

    elif Category == "2":

        subcategory = input('1. AC - Van \n2. NonAC - Van \nEnter your Choice :')

        if subcategory == '1':

            nic = input('Enter Customer NIC :')
            if nic in Reserved_Van_AC.keys():

                print(nic, ' Hired ', Reserved_Van_AC[nic])
                RemoveRq = input('Do You want to Release This vehicle ? \n1. Yes \n2. NO \nEnter your choice : ')

                if RemoveRq == '1':
                    temp = Reserved_Van_AC[nic]
                    Van_AC.insert(0, temp)
                    Reserved_Van_AC.pop(nic)
                    print(temp, 'is Successfully Released')

                if RemoveRq == '2':
                    print('Task Canceled. You will be redirected to Home menu')

            else:
                print('No AC - Van Reserved for this NIC')


        elif subcategory == "2":

            nic = input('Enter Customer NIC :')

            try:
                if nic in Reserved_Van_NonAC.keys():
                    print(nic, ' Hired ', Reserved_Van_NonAC[nic])

                    RemoveRq = input('Do You want to Release This vehicle ? \n1. Yes \n2. NO \nEnter your choice : ')

                    if RemoveRq == '1':
                        temp = Reserved_Van_NonAC[nic]
                        Van_NonAC.insert(0, temp)
                        Reserved_Van_NonAC.pop(nic)
                        print(temp, 'is Successfully Released')

                    if RemoveRq == '2':
                        print('Task Canceled. You will be redirected to Home menu')

                else:
                    print('No NonAC - Van Reserved for this NIC')
            except:
                print('check input')

        else:
            print('Invalid input')

    elif Category == "3":

        nic = input('Enter Customer NIC :')

        try:
            if nic in Reserved_3Wheel.keys():
                print(nic, ' Hired ', Reserved_3Wheel[nic])

                RemoveRq = input('Do You want to Release This vehicle ? \n1. Yes \n2. NO \nEnter your choice : ')

                if RemoveRq == '1':
                    temp = Reserved_3Wheel[nic]
                    _3Wheel.insert(0, temp)
                    Reserved_3Wheel.pop(nic)
                    print(temp, 'is Successfully Released')

                if RemoveRq == '2':
                    print('Task Canceled. You will be redirected to Home menu')

            else:
                print('No 3Wheel Reserved for this NIC')
        except:
            print('check input')

    elif Category == "4":

        subcategory = input('1. AC - Van \n2. NonAC - Van \nEnter your Choice :')

        if subcategory == '1':

            nic = input('Enter Customer NIC :')

            try:
                if nic in Reserved_Truck_7ft.keys():
                    print(nic, ' Hired ', Reserved_Truck_7ft[nic])

                    RemoveRq = input('Do You want to Release This vehicle ? \n1. Yes \n2. NO \nEnter your choice : ')

                    if RemoveRq == '1':
                        temp = Reserved_Truck_7ft[nic]
                        Truck_7ft.insert(0, temp)
                        Reserved_Truck_7ft.pop(nic)
                        print(temp, 'is Successfully Released')

                    if RemoveRq == '2':
                        print('Task Canceled. You will be redirected to Home menu')

                else:
                    print('No Truck 7ft Reserved for this NIC')
            except:
                print('check input')

        elif subcategory == "2":

            nic = input('Enter Customer NIC :')

            try:
                if nic in Reserved_Truck_12ft.keys():
                    print(nic, ' Hired ', Reserved_Truck_12ft[nic])

                    RemoveRq = input('Do You want to Release This vehicle ? \n1. Yes \n2. NO \nEnter your choice : ')

                    if RemoveRq == '1':
                        temp = Reserved_Truck_12ft[nic]
                        Truck_12ft.insert(0, temp)
                        Reserved_Truck_12ft.pop(nic)
                        print(temp, 'is Successfully Released')

                    if RemoveRq == '2':
                        print('Task Canceled. You will be redirected to Home menu')

                else:
                    print('No Truck 12ft Reserved for this NIC')
            except:
                print('check input')

        else:
            print('Invalid input')

    elif Category == "5":

        subcategory = input('1. AC - Van \n2. NonAC - Van \nEnter your Choice :')

        if subcategory == '1':

            nic = input('Enter Customer NIC :')

            try:
                if nic in Reserved_Lorry_2500.keys():
                    print(nic, ' Hired ', Reserved_Lorry_2500[nic])

                    RemoveRq = input('Do You want to Release This vehicle ? \n1. Yes \n2. NO \nEnter your choice : ')

                    if RemoveRq == '1':
                        temp = Reserved_Lorry_2500[nic]
                        Lorry_2500.insert(0, temp)
                        Reserved_Lorry_2500.pop(nic)
                        print(temp, 'is Successfully Released')

                    if RemoveRq == '2':
                        print('Task Canceled. You will be redirected to Home menu')

                else:
                    print('No Lorry 2500KG Reserved for this NIC')
            except:
                print('check input')

        elif subcategory == "2":

            nic = input('Enter Customer NIC :')

            try:
                if nic in Reserved_Lorry_3500.keys():
                    print(nic, ' Hired ', Reserved_Lorry_3500[nic])

                    RemoveRq = input('Do You want to Release This vehicle ? \n1. Yes \n2. NO \nEnter your choice : ')

                    if RemoveRq == '1':
                        temp = Reserved_Lorry_3500[nic]
                        Lorry_3500.insert(0, temp)
                        Reserved_Lorry_3500.pop(nic)
                        print(temp, 'is Successfully Released')

                    if RemoveRq == '2':
                        print('Task Canceled. You will be redirected to Home menu')

                else:
                    print('No Lorry 3500KG Reserved for this NIC')
            except:
                print('check input')

        else:
            print('Invalid input')


def reserved():
    print('Vehicle Categories : \n1 - Car \n2 - Van\n3 - 3 Wheelers\n4 - Truck\n5 - Lorry\n')
    Category = input('Enter Category : ')

    if Category == '1':
        if len(Reserved_Car_AC) > 0:
            print('\n-- Reserved Vehicle in CAR - AC --\nPerson NIC --> Vehicle NO')
            for x, no in Reserved_Car_AC.items():
                print(x, " --> ", no)

        else:
            print('\nNo Reserved Vehicle in CAR - AC')

        if len(Reserved_Car_NonAC) > 0:
            print('\n-- Reserved Vehicle in CAR - NonAC -- \nPerson NIC --> Vehicle NO')
            for x, no in Reserved_Car_NonAC.items():
                print(x, " --> ", no)

        else:
            print('\nNo Reserved Vehicle in CAR - NonAC')

    elif Category == '2':
        if len(Reserved_Van_AC) > 0:
            print('\n-- Reserved Vehicle in VAN - AC -- \nPerson NIC --> Vehicle NO')
            for x, no in Reserved_Van_AC.items():
                print(x, " --> ", no)

        else:
            print('\nNo Reserved Vehicle in VAN - AC')

        if len(Reserved_Van_NonAC) > 0:
            print('\n-- Reserved Vehicle in Van - NonAC -- \nPerson NIC --> Vehicle NO')
            for x, no in Reserved_Van_NonAC.items():
                print(x, " --> ", no)

        else:
            print('\nNo Reserved Vehicle in Van - NonAC')

    elif Category == '3':
        if len(Reserved_3Wheel) > 0:
            print('\n-- Reserved Vehicle in 3 Wheeler -- \nPerson NIC --> Vehicle NO')
            for x, no in Reserved_3Wheel.items():
                print(x, " --> ", no)

        else:
            print('\nNo Reserved Vehicle in 3 Wheeler')


    elif Category == '4':
        if len(Reserved_Truck_7ft) > 0:
            print('\n-- Reserved Vehicle in Truck 7ft -- \nPerson NIC --> Vehicle NO')
            for B, no in Reserved_Truck_7ft.items():
                print(B, " --> ", no)

        else:
            print('\nNo Reserved Vehicle in Truck 7ft')

        if len(Reserved_Truck_12ft) > 0:
            print('\n-- Reserved Vehicle in Truck 12ft -- \nPerson NIC --> Vehicle NO')
            for x, no in Reserved_Truck_12ft.items():
                print(x, " --> ", no)

        else:
            print('\nNo Reserved Vehicle in Truck 12ft')


    elif Category == '5':
        if len(Reserved_Lorry_2500) > 0:
            print('\n-- Reserved Vehicle in Lorry 2500KG -- \nPerson NIC --> Vehicle NO')
            for k, no in Reserved_Lorry_2500.items():
                print(k, " --> ", no)

        else:
            print('\nNo Reserved Vehicle in Lorry 2500KG')

        if len(Reserved_Lorry_3500) > 0:
            print('\n-- Reserved Vehicle in Lorry 3500KG -- \nPerson NIC --> Vehicle NO')
            for x, no in Reserved_Lorry_3500.items():
                print(x, " --> ", no)

        else:
            print('\nNo Reserved Vehicle in Lorry 3500KG')

    else:
        print('Check your input for Vehicle type in Reserved Vehicle')


def view_vehicle():
    print('Vehicle Categories : \n1 - Car \n2 - Van\n3 - 3 Wheelers\n4 - Truck\n5 - Lorry')
    Category = input('Enter Category : ')

    try:
        _Category = int(Category)

    except:
        print('Check your input')

    if _Category == 1:

        if len(Car_AC) != 0:

            print('\nCAR - AC :')
            for num in Car_AC:
                print(num)

        else:
            print('\nNo vehicles in Car - AC')

        if len(Car_NonAC) != 0:

            print('\nCAR - NonAC :')
            for num in Car_NonAC:
                print(num)
        else:
            print('\nNo vehicles in Car - NonAC')


    elif _Category == 2:

        if len(Van_AC) != 0:
            print('\nVAN - AC :')
            for num in Van_AC:
                print(num)

        else:
            print('\nNo vehicles in Van - AC')

        if len(Van_NonAC) != 0:
            print('\nVAN - NonAC :')
            for num in Van_NonAC:
                print(num)

        else:
            print('\nNo vehicles in Car - NonAC')


    elif _Category == 3:
        if len(_3Wheel) != 0:
            print('\n3 Wheelers :')
            for num in _3Wheel:
                print(num)
        else:
            print('\nNo vehicles in 3 Wheelers')

    elif _Category == 4:

        if len(Truck_7ft) != 0:
            print('\nTruck - 7ft :')
            for num in Truck_7ft:
                print(num)

        else:
            print('\nNo vehicles in Truck - 7ft')

        if len(Truck_12ft) != 0:
            print('\nTruck - 12ft :')
            for num in Truck_12ft:
                print(num)

        else:
            print('\nNo vehicles in Truck - 12ft')

    elif _Category == 5:
        if len(Lorry_2500) != 0:
            print('\nLorry - 2500KG :')
            for num in Lorry_2500:
                print(num)

        else:
            print('\nNo vehicles in Lorry - 2500KG')

        if len(Lorry_3500) != 0:
            print('\nLorry - 3500KG :')
            for num in Lorry_3500:
                print(num)

        else:
            print('\nNo vehicles in Lorry - 3500KG')
    else:
        print('\nError. Check your input')


def save_data():
    try:
        pickle.dump(Car_AC, open('data/CarAC.dat', 'wb'))
        pickle.dump(Car_NonAC, open('data/Car_NonAC.dat', 'wb'))
        pickle.dump(Van_AC, open('data/Van_AC.dat', 'wb'))
        pickle.dump(Van_NonAC, open('data/Van_NonAC.dat', 'wb'))
        pickle.dump(_3Wheel, open('data/_3Wheel.dat', 'wb'))
        pickle.dump(Truck_7ft, open('data/Truck_7ft.dat', 'wb'))
        pickle.dump(Truck_12ft, open('data/Truck_12ft.dat', 'wb'))
        pickle.dump(Lorry_2500, open('data/Lorry_2500.dat', 'wb'))
        pickle.dump(Lorry_3500, open('data/Lorry_3500.dat', 'wb'))

        pickle.dump(Reserved_Car_AC, open('data/Reserved_Car_AC.dat', 'wb'))
        pickle.dump(Reserved_Car_NonAC, open('data/Reserved_Car_NonAC.dat', 'wb'))
        pickle.dump(Reserved_Van_AC, open('data/Reserved_Van_AC.dat', 'wb'))
        pickle.dump(Reserved_Van_NonAC, open('data/Reserved_Van_NonAC.dat', 'wb'))
        pickle.dump(Reserved_3Wheel, open('data/Reserved_3Wheel.dat', 'wb'))
        pickle.dump(Reserved_Truck_7ft, open('data/Reserved_Truck_7ft.dat', 'wb'))
        pickle.dump(Reserved_Truck_12ft, open('data/Reserved_Truck_12ft.dat', 'wb'))
        pickle.dump(Reserved_Lorry_2500, open('data/Reserved_Lorry_2500.dat', 'wb'))
        pickle.dump(Reserved_Lorry_3500, open('data/Reserved_Lorry_3500.dat', 'wb'))

        print('Data has been saved successfully')

    except:
        print('Unable to save data.')


def clear():
    os.system('CLS')


print('Welcome to Cab Service !!')

RunProgram = True

while RunProgram:

    print('\nChoose your Task : \n1 - Add new vehicle \n2 - Remove vehicle\n3 - Reserve Vehicle\n4 - Release Vehicle'
          '\n5 - View Reserved Vehicle Details \n6 - Vehicles in Category\n7 - Clear Console\n8 - Exit\n')

    try:
        task = int(input('Your Input : '))

        if task == 1:
            add_vehicle()

        elif task == 2:
            remove_vehicle()

        elif task == 3:
            reserve()

        elif task == 4:
            release()

        elif task == 5:
            reserved()

        elif task == 6:
            view_vehicle()

        elif task == 7:
            clear()

        elif task == 8:
            save_data()
            print('Program Terminated.')
            RunProgram = False

        else:
            print('Invalid Input')

    except:
        print('Enter only a value.')

