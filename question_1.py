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
    def __init__(self, f_number, cap, dep, arr, conf_p, wait_p):
        self.f_number = f_number
        self.cap = cap
        self.dep = dep
        self.arr = arr
        self.conf_p = conf_p
        self.wait_p = wait_p

# Data initialization
command_list = ['addpassenger', 'addflight', 'flightlist', 'flightrates', 'help', 'exit', '']
command = ''
passenger_list = []
flight_list = []

# Body code
while command not in command_list or command != 'exit': # Repeats body until exit command is given
    print("What would you like to do?\n"+
      "--------------------------\n"+
      "addpassenger - To enter a new passengers details\n"+
      "addflight - To schedule a new flight\n"+
      "flightlist - To display all passenger info of a flight\n"+
      "flightrates - To check for flight occupancy rates\n"+
      "help - For list of commands\n"+
      "exit - To end program\n")

    command = input("Enter a command: ")
    print("Entered command: " + command)

    if command == "addpassenger":
        print("Command - addpassenger\n")

        name        = input("Enter name: ")
        pp_number   = input("Enter passport number: ")
        DOB         = input("Enter Date of Birth: ")
        membership  = input("Enter membership status: ")

        name = passenger(name, pp_number, DOB, membership)

        passenger_list.append(name)
        print("\nPassenger successfully created!\n"+
            "Passenger details as follows: \n"+
            "Name: " + name.name +
            "\nPassport number: " + name.pp_number +
            "\nDOB: " + name.DOB + 
            "\nMembership: " + name.membership + "\n\n")

    elif command == "addflight":
        print("Command - addflight\n")

        f_number    = input("Enter flight number: ")
        cap         = input("Enter maximum capacity: ")
        dep_date    = input("Enter departure date: ")
        dep_time    = input("Enter departure time: ")
        dep_loc     = input("Enter departure location: ")
        arr_date    = input("Enter arrival date: ")
        arr_time    = input("Enter arrival time: ")
        arr_loc     = input("Enter arrival location: ")

        dep = dep_arr(dep_date, dep_time, dep_loc)
        arr = dep_arr(arr_date, arr_time, arr_loc)

        f_number = flight(f_number, cap, dep, arr, [], [])

        flight_list.append(f_number.f_number)

        print("Flight successfully created!\n")
        print("Flight number: " + f_number.f_number)
        print("\nMaximum capacity: " + f_number.cap)
        print("\nDeparting: " + f_number.dep.date + ", " + f_number.dep.time + " from " + f_number.dep.loc)
        print("\nArrival: " + f_number.arr.date + ", " + f_number.arr.time + " at " + f_number.arr.loc)
        

    elif command == "flightlist":
        print("Command - flightlist\n")
        
        print("Total number of flights: " + str(len(flight_list)) + "\n")
        print(flight_list)

    elif command == "flightrates":
        print("Command - flightrates\n")

    elif command == "help":
        print("Command - help\n")

    elif command == "exit":
        print("Command - exit\n")

        print("All data will be lost on exit.\n")
        exit_confirm = input("To confirm you wish to exit, enter \"CONFIRM\": ")
        if exit_confirm != "CONFIRM":
            command = ""

    elif command not in command_list:
        print("Command not recognised. Please enter a recognised command.\n")

