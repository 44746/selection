#George West
#6-10-2014
#Maths

num1=int(input("Please enter your first number: "))
num2=int(input("Please enter your second number: "))
print("""Your options are:
m for multiply
d for divide
a for add
s for subtract""")
choice=input("Please enter your choice: ")
if choice =='m' or choice =='d' or choice =='a' or choice =='s':
    if choice == 'm':
        answer = num1*num2
    elif choice == 'd':
        answer= num1/num2
    elif choice=='a':
        answer= num1+num2
    else:
        answer= num1-num2
    print("Your answer is {0}".format(answer))
else:
    print("invalid character entered")
