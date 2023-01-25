my_name = "Burak Can Alagoz"
my_id = "190102002006"
my_email = "b.alagoz2019@gtu.edu.tr"

def problem1():
    return f"Hi all, This is {my_name}!"


def problem2():
    text = input("Enter some input:")
    # return 'Input was ' +text
    return f"Input was {text}"


def problem3():
    first_number = int(input("Enter first number:"))
    second_number = int(input("Enter second number:"))
    return first_number + second_number


def problem4():
    first_number = float(input("Enter first number:"))
    second_number = float(input("Enter second number:"))
    return first_number - second_number


def problem5():
    first_number = int(input("Enter first number:"))
    second_number = int(input("Enter second number:"))
    return first_number % second_number


def problem6():
    pi = 3.141592
    radius = float(input("Enter radius:"))
    height = float(input("Enter height:"))
    return pi * (radius * radius) * height


def problem7():
    side = float(input("Enter one side:"))
    p = 4 * side
    return f'The perimeter of the square is {p}.' 


if __name__ == '__main__':
    print(f"My name is {my_name}.")
    print(f"My number is {my_id}.")
    print(f"My email is {my_email}.")
    
    print(problem1())
    print(problem2())
    print(problem3())
    print(problem4())
    print(problem5())
    print(problem6())
    print(problem7())
