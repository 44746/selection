year = int(input("Please input the number of the year: e.g 2013  "))
century = year == 2000
if century %400 == 0:
     print("It is/was a leap year")
elif year%4 == 0:
     print("It is/was a leap year ")
else:
     print("It isnt/wasnt a leap year") 
