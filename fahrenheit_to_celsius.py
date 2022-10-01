def convert(s):
    f = float(s)
    c = (f - 32) * 5/9
    return c
celsius = input("Enter values in Fahrenheit: ")
convert(celsius)    