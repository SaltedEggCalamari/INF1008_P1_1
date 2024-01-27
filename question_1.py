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

        name        = input("Enter a name: ")
        pp_number   = input("Enter passport number: ")
        DOB         = input("Enter Date of Birth: ")
        membership  = input("Enter membership status: ")

        name = passenger(name, pp_number, DOB, membership)

        passenger_list.append(name)
        print("\nPassenger successfully created!\n"+
            "Passenger details as follows: \n"+
            "Name: " + passenger_list[0].name +
            "\nPassport number: " + passenger_list[0].pp_number +
            "\nDOB: " + passenger_list[0].DOB + 
            "\nMembership: " + passenger_list[0].membership + "\n\n")

    elif command == "addflight":
        print("Command - addflight\n")

    elif command == "flightlist":
        print("Command - flightlist\n")

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


