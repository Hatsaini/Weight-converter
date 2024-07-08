while True:
    try:
        weight = float(input('weight: '))
        break
    except ValueError:
        print('invalid input. Please enter a number')

unit = input('(L)bs or (K)g: ').upper()

while unit not in ['L', 'K']:
    print('invalid input. Please enter "L" for pounds or "K" for kilograms.')
    unit = input('(L)bs or (K)g: ').upper()

if unit== "L":
    converted = weight * 0.45359237  
    print(f"your weight is {converted} kilos")
else:
    converted = weight / 0.45359237
    print(f"your weight is {converted} pounds")
