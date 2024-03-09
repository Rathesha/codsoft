#print("Select an operation to perform:")
print("1,ADD")
print("2,SUBTRACT")
print("3,MULTIPLY")
print("4,DIVIDE")
operation=input("Enter the operation : ")
if(operation=="1"):
    a=int(input("Enter the number1: "))
    b=int(input("Enter the number2"))
    print("The sum is " + str(a+b))
    a=input("Enter the number1: ")
    b=input("Enter the number2: ")
elif(operation=="2"):
     a=int(input("Enter the number1: "))
     b=int(input("Enter the number2: "))
     print("The difference is " + str(a-b));
elif(operation=="3"):
    a=int(input("Enter the number1:"))
    b=int(input("Enter the number2: "))
    print("The  Multiply is " + str(a*b))
elif(operation=="4"):
    a=int(input("Enter the number1: "))
    b=int(input("Enter the number2: "))
    print("The divide is " +str(a/b))
else:
    print("Invalid entry")
