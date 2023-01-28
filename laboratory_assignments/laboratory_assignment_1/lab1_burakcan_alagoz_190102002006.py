
my_name = "Burak Can Alagoz"
my_id = "190102002006"
my_email = "b.alagoz2019@gtu.edu.tr"


def problem1():
    
    return my_name[0]

def problem2():
    
    number = int(input("Enter a number: ")) % len(my_name)
    
    return my_name[number]
    
def problem3():
    
    input1 = int(input("Enter first number: ")) % len(my_name)
    input2 = int(input("Enter second number: ")) % len(my_name)
    
    if input1 > input2:
        return my_name[input2:input1+1]
    else:
        return my_name[input1:input2+1]


def problem4():
    string = input("Enter string:")
    vowels = 0
    for i in string:
        if(i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']):
            vowels = vowels + 1
    
    return vowels

def problem5():
    sum = 0

    for digit in my_id: 
      sum += int(digit)      
    
    return sum

def problem6():
    
    num = int(input("Enter input: ")) 
    
    factorial = 1  
    
    if num <= 30:    
        for i in range(1,num + 1):
            factorial = factorial*i      
             
    return factorial
   
def problem7():
    
    num = int(input("Enter input: ")) 
    
    if num % 3 == 0 and num % 7 == 0:
        return True
    else:
        return False
    
def problem8():
    
    num = int(input("Enter input: ")) 
    
    if num % 3 == 0 and num % 7 == 0:
        return 3
    elif num % 3 == 0 :
        return 1
    elif num % 7 == 0 :
        return 2
    else:
        return num
        # There is no case for other input in PDF. returned number
    
def problem9():
    
    num = int(input("Enter a number: ")) 
    
    if num > 1:
        for i in range(2,num):
             if (num%i) == 0:
                return False
        return True
    return False
    
def problem10():
    
    num = float(input("Enter a number: ")) 
    
    x0 = num/2
    difference = 1
    accuracy = 0.00000001
    
    while difference > accuracy:
        x1 = 0.5 * (x0 + (num/x0))
        difference = x0 - x1
        x0 = x1
    return x0
    
    


if __name__ == "__main__":
    
    print(f"My name is {my_name}.")
    print(f"My number is {my_id}.")
    print(f"My email is {my_email}.")

    
    print("Running problem 1")
    print( problem1() )

    print("Running problem 2")
    print( problem2() )
    
    print("Running problem 3")
    print( problem3() )

    print("Running problem 4")
    print( problem4() )
    
    print("Running problem 5")
    print( problem5() )
    
    print("Running problem 6")
    print( problem6() )
    
    print("Running problem 7")
    print( problem7() )
    
    print("Running problem 8")
    print( problem8() )
    
    print("Running problem 9")
    print( problem9() )
    
    print("Running problem 10")
    print( problem10() )