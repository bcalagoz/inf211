my_name = "Burak Can Alagoz"
my_id = "190102002006"
my_email = "b.alagoz2019@gtu.edu.tr"


def problem1(s):
    for char in s:
        if char == "K":
            return True

    return False


def problem2(a,b,c,d):
    list = [a,b,c,d]
    list.sort()

    return list[0]

def problem3(x, y):
    if x >= 0:
        if x >= int(y + 0.5):
            return int(x)
        elif x < int(y + 0.5):
            return round(x)

    elif x < 0:
        if y >= 0:
            return int(x)
        elif y < 0:
            return round(x)    

def problem4(radius,height,pi = 3.1415):
    return height * pi * (radius**2)


def problem5(radius,height,pi = 3.1415):
    if (isinstance(radius, float) or isinstance(radius, int)) and (isinstance(height, float) or isinstance(height, int)):
        return height * pi * (radius**2)

    return -1


def problem6(text):
    for char in text:
        if (text.find(char, (text.find(char)+1))) == -1:
            return char


def problem7(text):

	n = len(text)

	for i in range(1, n):

		if (text[i] < text[i - 1]) :
			return False

	return True


def problem8(text):
    
    for i in range(len(text)):
        for j in range(i+1,len(text)):
            if (text[i] == text[j]):
                return False
    return True

def problem9(row,column):
    if row == 1 and column == 1:
        return 1
    elif row > 1 and column == 1:
        return 3
    elif row > 1 and column == row:
        return 2    

    return problem9(row-1,column-1) + problem9(row-1,column)


def problem10(text1,text2):
    if len(text1) <= len(text2):

        count = 0

        for i in range(len(text1)):
            if text1[i] == text2[i]:
                count += 1

        return count

    elif len(text1) > len(text2):

        count = 0

        for i in range(len(text2)):
            if text1[i] == text2[i]:
                count += 1

        return count

def problem11(x, y):

    if y%1==0.5 and y>0:
        rndy= y+0.5
    
    elif y%1==0.5 and y<0:
        rndy= y-0.5
    else:
        rndy=round(y)
        
    if x<0 and rndy<x: 
        return int(x)-1
    
    elif x<0:
        return int(x)
    
    elif x>rndy:
        return int(x)
    
    elif x==int(x):
        return int(x)
    
    else: 
        return int(x)+1
