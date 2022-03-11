log_file = open("um-server-01.txt")  # Opening the File


def sales_reports(log_file):  # Declaring function with param
    for line in log_file:   # Creating a for loop
        line = line.rstrip()    # Stripping the line (Not that way you perv)
        day = line[0:3]     # Setting day equal to an index in the line
        if day == "Mon":    # Checking to see if day is equal to Tuesday
            print(line)     # If it is, it will print the line


sales_reports(log_file)     # Invoking the function
