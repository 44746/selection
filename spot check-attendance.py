#George West
#10-10-2014
#Attendance
attendance = int(input("Please input the percentage of your attendance: "))
if 0<= attendance<=100:
    if attendance > 84:
        print("Your attendance is {0}%. Keep up the good attendance.".format(attendance))
    else:
        print("Your attendance is only {0}%. You must improve your attendance.".format(attendance))
else:
    print("Invalid percentage entered")
