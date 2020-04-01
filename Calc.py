import re

print("Welcome to my calculator")


def get_value():
    """
    User input value.
    """
    val = str(input(f"{msg}")).replace(",", ".")
    return val


def test_value():
    """Function checks user input for a decimal numbers and mathematical actions.
    Added check for exclude 'leading zero'.
    """
    while True:
        val = get_value()
        # Регулярка делится на: (Целые числа |С плавающей точкой | Отрицательные целые числа |Отрицательные с плавающей точкой)
        r_nums = re.match(r"^[0-9]*$|^[0-9]*\.[0-9]*$|^\-[0-9]*$|^\-[0-9]*\.[0-9]*$", val)
        # Регулярка действия
        r_action = re.match(r"^[\+\-\*\/]{1}$", val)

        if not ((r_nums and i % 2 == 0 and val) or (r_action and i % 2 == 1 and val)):
            print("Incorrect value! repeat Entry!")
        else:
            while val[0] == "0" and len(val) > 1:
                val = val[1:]
            else:
                return val


def calc():
    """Function for adding a String value from input.
    """
    str1 = ""
    s = 3
    global msg, i  # msg Global declaration for user input
    msg = ""
    for i in range(s):
        if i % 2 != 0:
            msg = "Enter an action: "
        else:
            msg = "Enter some number: "
        # writes iterable value in string
        str1 += test_value()
    return str1


try:
    res = eval(calc())
    print((res))
except ZeroDivisionError:
    print("You cant divide by zero!")
