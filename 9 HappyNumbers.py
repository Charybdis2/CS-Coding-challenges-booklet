def is_happy_number(number):
    """Prints if it is a happy number or not """
    total = 0
    while (total != 4) and (total != 1):
        total = 0
        for numL in [int(a) for a in str(number)]:
            total += numL ** 2
        number = total
        print(total)
    if total == 1:
        print("Is a happy number")
    else:
        print("Very sad number")
number = input("Please input a positive integer: ")
is_happy_number(number)

