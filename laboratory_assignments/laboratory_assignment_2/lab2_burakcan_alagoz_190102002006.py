my_name = "Burak Can Alagoz"
my_id = "190102002006"
my_email = "b.alagoz2019@gtu.edu.tr"


def problem1():
    temperatureFah = float(input("Enter Fahrenheit degree: "))
    temperatureCel = float(((temperatureFah - 32) * 5) / 9)

    return temperatureCel


def problem2():
    temperatureCel = float(input("Enter Celsius degree: "))
    temperatureFah = float((temperatureCel * 1.8) + 32)

    return temperatureFah


def problem3():
    num = int(input("Enter a number: "))
    hexagonalNumber = (2 * (num * num)) - num

    return hexagonalNumber


def problem4():
    n = int(input("Enter a number: "))

    x0 = 2
    x1 = 1

    if (n == 0):
        return x0

    for i in range(2, n + 1):
        l = x0 + x1
        x0 = x1
        x1 = l

    return x1


def problem5():
    s = input("Enter a string: ")

    return s[::-1]


def problem6():
    s = input("Enter a string: ")
    s1 = "".join(c for c in s if c.isalnum())
    return s1


def problem7():
    s = input("Enter input: ")
    s = int(s)
    is_minus = False
    if s == 0:
        return "0"

    if s < 0:
        s *= -1
        is_minus = True

    digits = ""
    while s:
        digits += str(int(s % 4))
        s //= 4

    if is_minus:
        return "-" + digits[::-1]
    else:
        return digits[::-1]


def problem8():
    text = input("Enter input: ")

    if len(text) % 2 != 0:
        return False

    dictionary = {'{': '}', '(': ')', '[': ']'}
    stack = []

    for char in text:
        if char in dictionary.keys():
            stack.append(char)
        else:
            if stack == []:
                return False
            brace = stack.pop()
            if char != dictionary[brace]:
                return False
    return stack == []


def problem9():
    text = input("Enter a string: ")
    listText = list(text.split(" "))

    return len(listText[-1])


def problem10():
    route = input("Enter the exit route: ")
    current_x = 0
    current_y = 0
    for step in route:
        if step == 'e':
            current_x += 1
        elif step == 'w':
            current_x -= 1
        elif step == 'n':
            current_y += 1
        elif step == 's':
            current_y -= 1
    
    return ((abs(current_x - 0) ** 2) + (abs(current_y - 0) ** 2)) ** (1/2)


if __name__ == "__main__":
    print(f"My name is {my_name}.")
    print(f"My number is {my_id}.")
    print(f"My email is {my_email}.")

    print("Running problem 1")
    print(problem1())

    print("Running problem 2")
    print(problem2())

    print("Running problem 3")
    print(problem3())

    print("Running problem 4")
    print(problem4())

    print("Running problem 5")
    print(problem5())

    print("Running problem 6")
    print(problem6())

    print("Running problem 7")
    print(problem7())

    print("Running problem 8")
    print(problem8())

    print("Running problem 9")
    print(problem9())

    print("Running problem 10")
    print(problem10())