def CelsiusToFahrenheit():
    f = (c*(9/5))+32

    return f

c = float(input("Input temperature in degree Celcius: "))

print("The degree in Fahrenheit is ",CelsiusToFahrenheit())