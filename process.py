log_file = open("um-server-01.txt")  # Opening the File


# def sales_reports(log_file):  # Declaring function with param
#     for line in log_file:   # Creating a for loop
#         line = line.rstrip()    # Stripping the line (Not that way you perv)
#         print(line)
#         day = line[0:3]     # Setting day equal to an index in the line
#         print(day)
#         if day == "Mon":    # Checking to see if day is equal to Tuesday (Now Monday after changing it)
#             print(line)     # If it is, it will print the line


# sales_reports(log_file)     # Invoking the function

def melon_stuff(log_file):
    for line in log_file:
        line = line.rstrip()
        values = line.split(' ')
        total = int(values[2])
        if total >= 10:
            print(line)

melon_stuff(log_file)