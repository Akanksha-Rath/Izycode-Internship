def add(num1,num2):
    sum = num1 + num2
    return sum


def sub(num1,num2):
    sub = num1 - num2
    return sub


def mul(num1,num2):
    mul = num1*num2
    return mul


def div(num1,num2):
    div = num1/num2
    return div


while True:
    num1 = int(input("Enter a no. : "))
    num2 = int(input("Enter another no. : "))

    choice = int(input("Enter a choice : \n0 for Exiting\n1 for Adding\n2 for Subtracting\n3 for Multiplying\n4 for Dividing "))
    if choice == 1:
        x = add(num1,num2)
    elif choice == 2:
        x = sub(num1,num2)
    elif choice == 3:
        x = mul(num1,num2)
    elif choice == 4:
        x = div(num1,num2)
    elif choice == 0:
        break
    
    else:
        print("Wrong input,\nTry again")

    print(f"The result is",x)
