def fah_to_cel(string):
    temp_conv = (5/9)*(string-32)
    return temp_conv

def cel_to_fah(val):
    temp_conve = (val*(9/5))+32
    return temp_conve

temp = float(input("Enter the value of Temperature: "))
units = input("Enter the units for Temperature(F/C): ")

if (units == "F") or (units == "f"):
    print("The temperature in Celsius is: ", fah_to_cel(temp))
elif (units =="C") or (units == "c"):
    print("The temperature in Fahrenheit is: ", cel_to_fah(temp))
else:
    print(f"{units} is not a valid unit please enter a valid unit!!")
