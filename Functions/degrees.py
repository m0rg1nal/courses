def convert_degrees(value: float, units: str) -> str:
    if units == 'c':
        return f"{round((value + 1.8) + 32, 2)} Fahrenheit"
    if units == 'f':
        return f"{round((value - 32) / 1.8, 2)} Celsius"
    else:
        return "Please enter F or C, these are the only available units."


try:
    temp = input('Enter the temperature outside: ')
    value = int(temp.split(' ')[0])
    units = temp.split(' ')[1].lower()
    print(convert_degrees(value, units))
except:
    print('Please enter temperature like in this example: "12 C"')
