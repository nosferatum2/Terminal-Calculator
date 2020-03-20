import re

print("Welcome to my calculator")

def get_input():
    a = str(input("Enter some number: ")).replace(",",".")
    return a

def test_input():
    while True:
        a = get_input()
        # Регулярка делится на 3 блока: (Целые числа |С плавающей точкой | Действия)
        if not re.match(r"^[0-9]*$|^[0-9]*.[0-9]*$|^[\+\-\*\/]{1}$",a):
            print("Incorrect value! repeat Entry!")
        else:
            return a



def calc():
    txt = ""
    s = 3
    for i in range(s):
        txt += test_input()
    return txt


res = eval(calc())

print(res)
