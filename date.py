#George West
#30-09-2014
#date

day = int(input("Please input the number of the day: e.g 27  "))
month = int(input("Please input the number of the month: e.g 11  "))
year = int(input("Please input the number of the year: e.g 2013  "))



    
if 0<day<32 and 0<month<13 and 1820<year<2031:
    if month == 1:
        month = "January"
    elif month == 2:
        month = "February"
    elif month == 3:
        month = "March"
    elif month == 4:
        month = "April"
    elif month == 5:
        month = "May"
    elif month == 6:
        month = "June"
    elif month == 7:
        month = "July"
    elif month == 8:
        month = "August"
    elif month == 9:
        month = "September"
    elif month == 10:
        month = "October"
    elif month == 11:
        month = "November"
    elif month == 12:
        month = "December"
  
    if day == 1 or day == 21 or day == 31:
        ending ='st'
    elif day == 2 or day == 22:
        ending ='nd'
    elif day == 3 or day ==23:
        ending ='rd'
    else:
        ending = 'th'
    print("{0}{1} {2} {3}".format(day, ending, month, year))

    if year%100==0:
        
        if year %400 == 0:
            print("It is/was a leap year and a century")
        else:
            print("It isnt/wasnt a leap year")
    elif year%4 == 0:
        print("It is/was a leap year ")
    else:
        print("It isnt/wasnt a leap year")
else:
    print("You entered invalid data")
