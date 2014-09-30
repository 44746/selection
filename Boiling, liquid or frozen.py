#George West
#30-09-2014
#Boiling, liquid or frozen

temperature = float(input("Please enter the temperature: "))
if temperature >= 100:
    print("Boiling")
elif temperature > 0:
    print("Liquid")
else:
    print("Frozen")
