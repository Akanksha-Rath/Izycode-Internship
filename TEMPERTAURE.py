while True:

    temp_choice = int(input("Enter a  SCALE \n0 for Exit\n1 for celsius\n2 for fahreinheit\n3 for kelvin :\n"))
    if temp_choice==0:
        break
    temp = float(input("Enter the temperature you want to input: "))
    if temp_choice==1:
        print(f"fahrenheit value : {temp*(9/5)+32}F\nkelvin value : {temp + 273.15}K")
    elif temp_choice==2:
        print(f"celsius value : {(temp-32)*(5/9)}C\nkelvin value : {(temp-32)*(5/9) + 273.15}K")
    elif temp_choice==3:
        print(f"celsius value : {temp-273.15}C\nfahreinheit value : {(temp-273.15)*(9/5)+32}F")
    
    else:
        print("Wrong Input")
