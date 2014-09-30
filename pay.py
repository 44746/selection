#George West
#30-09-2014
#pay

hours = int(input("Please input the number of hours worked: "))
rate=int(input("Please input your hourly rate: "))
if hours < 61:
    if hours > 40:
        overtime = hours - 40
        overtime_pay = overtime*rate*1.5
        normal_pay = (hours - overtime) * rate
        pay= overtime_pay+normal_pay
        print("You will be payed {0} pounds".format(pay))
    elif 0<hours<40:
        pay = hours*rate
        print("You will be payed {0} pounds".format(pay))
    else:
        print("No hours worked")
else:
    print("ERROR- Too many hours")
