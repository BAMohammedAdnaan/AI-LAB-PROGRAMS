celsius=int(input("enter the temperature in celsius:"))
fahrenheit=(celsius*1.8)+32
print("%0.1f degree celsius is equal to %0.1f degree fahrenheit"%(celsius,fahrenheit))
if fahrenheit < 32:
    print("freezing weather")