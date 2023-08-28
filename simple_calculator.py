operation = input("calculation to perform,multiplication(M),division(D),subtraction(S), addition(A)? ").lower()
number_1 = input("first number: ")
number_2 = input("second number: ")
try:
    number_1, number_2 = float(number_1), float(number_2)
    if operation == 'm':
        result = number_1*number_2
        print("{} * {} = {}".format(number_1, number_2, result))
    elif operation == 'd':
        result = number_1/number_2
        print("{} / {} = {}".format(number_1, number_2, result))
    elif operation == 's':
        result = number_1 - number_2
        print("{} - {} = {}".format(number_1, number_2, result))
    elif operation == 's':
        result = number_1 + number_2
        print("{} + {} = {}".format(number_1, number_2, result))
    else:
        print("You entered invalid operation")

except:
    print("Invalid numbers")
