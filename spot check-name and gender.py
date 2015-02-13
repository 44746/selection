#George West
#10-10-2014
#Name and gender

first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
gender = input("Please enter your gender ( m or f): ")
if gender == "m" or gender == "M":
    print(" Mr {0} {1}".format(first_name, last_name))
elif gender == "f" or gender == "F":
    print ("Ms {0} {1}".format(first_name, last_name))
else:
    print("Please enter an appropriate gender")
    
