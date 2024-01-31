# Imports
import csv
import passenger_flight_generator


# Objects
class passenger:
    def __init__(self, name, pp_number, DOB, membership):
        self.name = name
        self.pp_number = pp_number
        self.DOB = DOB
        self.membership = membership
class dep_arr:
    def __init__(self, date, time, loc):
        self.date = date
        self.time = time
        self.loc = loc
class flight:
    def __init__(self, f_number, cap, dep, arr, conf_pax, wait_pax):
        self.f_number = f_number
        self.cap = cap
        self.dep = dep
        self.arr = arr
        self.conf_pax = conf_pax
        self.wait_pax = wait_pax


# Data initialization
command_list = ['addpassenger', 'addflight', 'loadfile', 'flightlist', 'checkflight', 'passengerlist', 'viewpassenger', 'flightrates', 'generatedata', 'assignpassengers', 'help', 'exit', '']
command = ''

passenger_list = []
g_passenger_list = []
s_passenger_list = []
n_passenger_list = []

flight_list = []
conf_pax_list = []
wait_pax_list = []


# Body code
while command not in command_list or command != 'exit': # Repeats body until exit command is given
    
    print("What would you like to do?\n")
    command = input("Enter a command: ")

    if command == "addpassenger": # (COMPLETED) Add new passenger to passenger list
        print("Command - addpassenger\n")

        name        = input("Enter name: ") # Get user input for passenger details
        pp_number   = input("Enter passport number: ")
        DOB         = input("Enter Date of Birth: ")
        membership  = input("Enter membership status: ")

        name = passenger(name, pp_number, DOB, membership) # Create new passenger object based on passenger name

        if name.membership == 'G': # Checks and sorts passengers based on membership status
            g_passenger_list.append(name)
        elif name.membership == 'S':
            s_passenger_list.append(name)
        elif name.membership == 'N':
            n_passenger_list.append(name)

        passenger_list = g_passenger_list + s_passenger_list + n_passenger_list # Collates passengers into a master name list that arrange according to membership status

        print("\nPassenger successfully created!\n"+ # Feedback to check passenger creation
            "Passenger details as follows: \n"+
            "Name: " + name.name +
            "\nPassport number: " + name.pp_number +
            "\nDOB: " + name.DOB + 
            "\nMembership: " + name.membership + "\n\n")

    elif command == "addflight": # (COMPLETED) Add new flight to flight list
        print("Command - addflight\n")

        f_number    = input("Enter flight number: ") # Gets user input for flight details
        cap         = input("Enter maximum capacity: ")
        dep_date    = input("Enter departure date: ")
        dep_time    = input("Enter departure time: ")
        dep_loc     = input("Enter departure location: ")
        arr_date    = input("Enter arrival date: ")
        arr_time    = input("Enter arrival time: ")
        arr_loc     = input("Enter arrival location: ")

        dep = dep_arr(dep_date, dep_time, dep_loc) # Creates dep_arr object to be inserted into flight object
        arr = dep_arr(arr_date, arr_time, arr_loc)

        f_number = flight(f_number, cap, dep, arr, [], []) # Creates flight object based on flight number

        flight_list.append(f_number) # Adds flight number to flight list

        print("Flight successfully created!\n") # Feedback to check flight creation
        print("Flight number: " + f_number.f_number)
        print("\nMaximum capacity: " + f_number.cap)
        print("\nDeparting: " + f_number.dep.date + ", " + f_number.dep.time + " from " + f_number.dep.loc)
        print("\nArrival: " + f_number.arr.date + ", " + f_number.arr.time + " at " + f_number.arr.loc)   

    elif command == "loadfile": # (COMPLETED) Loads passengers/flights from a .csv file
        print("Command - loadfile\n")
        # Entry types
        #
        # For passengers,
        # P,(name),(pp_number),(DOB),(membership)
        #
        # For flights,
        # F,(f_number),(cap),(dep date),(dep time),(dep loc),(arr date),(arr time),(arr loc)

        filename = input("Enter filename: ") # Get filename to open
        
        file = open(filename)
        reader = csv.reader(file) # Opens and reads file

        print("Loading file data, please wait\n")
        for row in reader: # Cycles through data from csv row by row
            if row[0] == 'P': # Passenger type entry handler

                name = row[1] # Gets passenger details from elements of row
                pp_number = row[2]
                DOB = row[3]
                membership = row[4]

                name = passenger(name, pp_number, DOB, membership)

                if name.membership == 'G': # Sorts passenger into memberships
                    g_passenger_list.append(name)
                elif name.membership == 'S':
                    s_passenger_list.append(name)
                elif name.membership == 'N':
                    n_passenger_list.append(name)

            elif row[0] == 'F': # Flight type entry handler

                f_number = row[1] # Get flight details from elements of row
                cap = row[2]
                dep_date = row[3]
                dep_time = row[4]
                dep_loc = row[5]
                arr_date = row[6]
                arr_time = row[7]
                arr_loc = row [8]

                dep = dep_arr(dep_date, dep_time, dep_loc) # Creates dep_arr object to be inserted into flight object
                arr = dep_arr(arr_date, arr_time, arr_loc)

                f_number = flight(f_number, cap, dep, arr, [], []) # Creates flight object based on flight number

                flight_list.append(f_number) # Adds flight number to flight list


            else: # Unknown entry handler
                print("Unrecognised entry, try again\n")
                break; # Stops loop once unknown entry is detected
        
        passenger_list = g_passenger_list + s_passenger_list + n_passenger_list # Collates membership lists into a master name list
        print("File data loaded\n")

    elif command == "flightlist": # (COMPLETED) View all flights
        print("Command - flightlist\n")
        
        for i in range(len(flight_list)):
            print(flight_list[i].f_number)
        
        print("Total number of flights: " + str(len(flight_list)) + "\n")

    elif command == "checkflight": # (COMPLETED) Check all passenger details of a flight
        print("Command - checkflight")

        f_number = input("Enter flight number: ")

        for i in range(len(flight_list)):
            if flight_list[i].f_number == f_number:
                print("Flight found!\n")
                f_number = flight_list[i]

                print("Flight number: " + f_number.f_number +
                      "\nCapacity: " + f_number.cap +
                      "\nDeparture on " + f_number.dep.date + " at time " + f_number.dep.time + " from " + f_number.dep.loc +
                      "\nArrival on " + f_number.arr.date + " at time " + f_number.arr.time + " from " + f_number.arr.loc + "\n")
                
                conf_pax_list = f_number.conf_pax
                wait_pax_list = f_number.wait_pax

                for i in range(len(conf_pax_list)):
                    print("Number of confirmed passengers: " + len(conf_pax_list) + "\n")
                    print("Passenger number: " + str(i)+
                          "\nName: " + conf_pax_list[i].name +
                          "\nPassport number: " + conf_pax_list[i].pp_number +
                          "\nDOB: " + conf_pax_list[i].DOB + 
                          "\nMembership: " + conf_pax_list[i].membership + "\n")
        
                for j in range(len(wait_pax_list)):
                    print("Number of waiting passengers: " + len(wait_pax_list) + "\n")
                    print("Passenger number: " + str(i)+
                          "\nName: " + wait_pax_list[i].name +
                          "\nPassport number: " + wait_pax_list[i].pp_number +
                          "\nDOB: " + wait_pax_list[i].DOB + 
                          "\nMembership: " + wait_pax_list[i].membership + "\n")
            
    elif command == "passengerlist": # (COMPLETED) View all passengers
        print("Command - passengerlist\n")
        
        for i in range(len(passenger_list)):
            print(passenger_list[i].name)
        print("Total number of passengers: " + str(len(passenger_list)) + "\n")

    elif command == "viewpassenger": # (COMPLETED) View passenger details
        print("Command - viewpassenger")

        name = input("Enter passenger name: ")

        for i in range(len(passenger_list)):
            if passenger_list[i].name == name:
                print("Passenger found!\n")
                name = passenger_list[i]

                print("Passenger name: " + name.name + 
                      "\nPassport number: " + name.pp_number +
                      "\nDOB: " + name.DOB + 
                      "\nMembership: " + name.membership + "\n")
                break                

    elif command == "flightrates": # (WORK IN PROGRESS) View flights with highest occupancies rates
        print("Command - flightrates\n")

    elif command == "generatedata": # (COMPLETED) Generates a csv file for n number of passengers and m number of flights
        print("Command - generatedata")

        n = input("Enter number of passengers to generate: ")
        m = input("Enter number of flights to generate: ")

        passenger_flight_generator.gen_passenger_flight(n, m)

    elif command == "assignpassengers": # (WORK IN PROGRESS) Runs algorithm to sort and assign passengers their seats
        print("Command - assignpassengers")

    elif command == "help": # (WORK IN PROGRESS) Normal Help function
        print("Command - help\n")
        print("addpassenger - To enter a new passengers details\n"+
              "addflight - To schedule a new flight\n"+
              "loadfile - To load a csv file for data\n"+
              "flightlist - To display all registered flights\n"+
              "checkflight - View all passenger details of a flight\n"+
              "passengerlist - To display all registered passengers\n"+
              "viewpassenger - View passenger details\n"+
              "flightrates - To check for flight occupancy rates\n"+
              "generatedata - To generate data of n passengers and m flights\n"+
              "assignpassengers - Assign passengers seats\n"+
              "help - For list of commands\n"+
              "exit - To end program\n")

    elif command == "exit": # (COMPLETED) Exits program
        print("Command - exit\n")

        exit_confirm = input("To confirm you wish to exit, enter \"CONFIRM\": ") # Confirms users request to exit program
        if exit_confirm != "CONFIRM":
            command = ""

    elif command not in command_list: # Loop to start sequence
        print("Command not recognised. Please enter a recognised command.\n")

    
                

