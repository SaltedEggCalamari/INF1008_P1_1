import csv

def gen_passenger_flight(n, m): # Generate a csv file containing n rows of passengers and m rows of flights

    filename = input("Enter filename to save: ") # Get user input to name file
    file = open(filename, 'w')
    writer = csv.writer(file)


    # Membership rates, non-members will be remaining
    G = 0.1 * float(n)
    G = int(G)
    S = 0.3 * float(n)
    S = int(S)


    for i in range(int(n)):
        name = 'N' + str(i).zfill(8)
        pp_number = 'P' + str(i).zfill(8)
        DOB = 'D' + str(i).zfill(8)
        
        if i < G:
            membership = 'G'
        elif i < S:
            membership = 'S'
        else:
            membership = 'N'

        row = ['P', name, pp_number, DOB, membership]
        writer.writerow(row)

    for j in range(int(m)):
        f_number = 'F' + str(j).zfill(8)
        cap = 600
        dep_date = 'DDATE' + str(j).zfill(8)
        dep_time = 'DTIME' + str(j).zfill(8)
        dep_loc = 'A'
        arr_date = 'ADATE' + str(j).zfill(8)
        arr_time = 'ATIME' + str(j).zfill(8)
        arr_loc = 'B'

        row = ['F', f_number, cap, dep_date, dep_time, dep_loc, arr_date, arr_time, arr_loc]
        writer.writerow(row)

    file.close()
