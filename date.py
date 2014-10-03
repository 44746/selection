#George West
#30-09-2014
#date

#pseudocode
#GET day
#GET month
#GET year
#IF year == 12 THEN
#   month = "December"
#IF year == 11 THEN
#   month = "November"
#IF year == 10 THEN
#   month = "October"
#IF year == 9 THEN
#   month = "September"
#IF year == 8 THEN
#   month = "August"
#IF year == 7 THEN
#   month = "july"
#IF year == 6 THEN
#   month = "June"
#IF year == 5 THEN
#   month = "May"
#IF year == 4 THEN
#   month = "April"
#IF year == 3 THEN
#   month = "March"
#IF year == 2 THEN
#   month = "February"
#IF year == 1 THEN
#   month = "January"
#IF day == 1 THEN
#        OUTPUT "1st {0} {1}" +month, year
#ELIF day == 21 THEN
#        OUTPUT "21st {0} {1}" +month, year
#ELIF day == 31 THEN
#        OUTPUT "31st {0} {1}" +month, year
#ELIF day == 2 THEN
#        OUTPUT "2ND {0} {1}" +month, year
#ELIF day == 22 THEN
#        OUTPUT "22ND {0} {1}" +month, year
#ELIF day == 3 THEN
#        OUTPUT "3RD {0} {1}" +month, year
# END IF
day = int(input("Please input the number of the day: e.g 27  "))
month = int(input("Please input the number of the month: e.g 11  "))
year = int(input("Please input the number of the year: e.g 2013  "))

if 0<day<32 and 0<month<13 and 1930<year<2031:
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
    
    if day == 1:
        print("1st {0} {1}" .format(month, year))
    elif day == 21:
        print("21st {0} {1}" .format(month, year))
    elif day == 31:
        print("31st {0} {1}" .format(month, year))
    elif day == 2:
        print("2nd {0} {1}" .format(month, year))
    elif day == 22:
        print("22nd {0} {1}" .format(month, year))
    elif day == 3:
        print("3rd {0} {1}" .format(month, year))
    elif day == 23:
        print("23rd {0} {1}" .format(month, year))

    else:
        print("{0} {1} {2}" .format(day, month, year))

else:
    print("You entered invalid data")
