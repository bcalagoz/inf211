my_name = "Burak Can Alagoz"
my_id = "190102002006"
my_email = "b.alagoz2019@gtu.edu.tr"




def problem1(list1,list_index):
    if list_index < 0 or list_index >= len(list1):
        return None
    else:
        return list1[list_index]


def problem2(list1,list_index):
    if list_index < 0 or list_index >= len(list1):
        return list1
    else:
        del list1[list_index]
        return list1

def problem3(list1,value):
    if value:
        value = False
    else:
        value = True 

    list1.sort(reverse=value)
    return list1

def problem4(l,w):
    numerator = 0
    denominator = 0

    for i in range(len(l)):
        numerator = numerator + (l[i] * w[i])
        denominator = denominator + w[i]

    return  numerator/denominator


def problem5(l1,l2):
    return len(set(l1) & set(l2))



def problem6(matrix):
    for i in range(len(matrix)):
        if len(matrix[i]) != len(matrix[0]):
            return None

    #1x1
    if len(matrix) == 1:
        return float(matrix[0][0])

    #2x2
    if len(matrix) == 2:
        return float((matrix[0][0] * matrix[1][1])-(matrix[0][1] * matrix[1][0]))

    #3x3
    if len(matrix) == 3:
        return float((matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[2][1] * matrix[1][2])-matrix[1][0] * (matrix[0][1] * matrix[2][2] - matrix[2][1] * matrix[0][2])+matrix[2][0] * (matrix[0][1] * matrix[1][2] - matrix[1][1] * matrix[0][2])))

    #4x4 
    if len(matrix) == 4:
        return float(matrix[0][0]*problem6([matrix[1][1:4], matrix[2][1:4], matrix[3][1:4]]) - (matrix[0][1] * problem6([[matrix[1][0], matrix[1][2], matrix[1][3]], [matrix[2][0], matrix[2][2], matrix[2][3]], [matrix[3][0], matrix[3][2], matrix[3][3]]])) + (matrix[0][2]*problem6([[matrix[1][0], matrix[1][1], matrix[1][3]],[matrix[2][0], matrix[2][1], matrix[2][3]],[matrix[3][0], matrix[3][1], matrix[3][3]]]))-matrix[0][3]*problem6([matrix[1][0:3], matrix[2][0:3], matrix[3][0:3]]))    



def problem7(accounts,source,lira,kurus):  
    digit_accounts = []
    transition = lira + float(kurus) / 100

    for i in range(len(accounts)):
        digit_accounts.append(float(accounts[i]))


    if source < 0 or source >= len(accounts):
        return accounts
    
    elif transition > digit_accounts[source]:
        return accounts

    else:
        digit_accounts[source] =  digit_accounts[source] - transition
        
        for i in range(len(digit_accounts)):
            if digit_accounts[i] % 1 == 0:
                accounts[i] = str('%.1f' % float( digit_accounts[i]))
            else:
                accounts[i] = str('%.2f' % float( digit_accounts[i]))
            
        return accounts



def problem8(accounts,source,destination,lira,kurus,fee=False):
    digit_accounts = []
    transition = lira + float(kurus) / 100
    fee_value = 0

    for i in range(len(accounts)):
        digit_accounts.append(float(accounts[i]))

    if source < 0 or destination < 0 or source >= len(accounts) or destination >= len(accounts) or transition > digit_accounts[source] or source==destination:
        return accounts
    

    elif fee == True and transition <= 10.0:
        fee_value = 0.1
        if digit_accounts[source] < transition + fee_value:
            return accounts
        
        digit_accounts[source] = digit_accounts[source] - transition - fee_value
        digit_accounts[destination] = digit_accounts[destination] + transition
        for i in range(len(digit_accounts)):
            if round(digit_accounts[i],2) % 1 == 0:
                accounts[i] = str('%.1f' % float( digit_accounts[i]))
            else:
                accounts[i] = str('%.2f' % float( digit_accounts[i]))
            if accounts[i] == '-0.0':
                accounts[i] = '0.0'

        return accounts

    elif fee == True and transition > 10.0:
        fee_value = float(transition) / 100
        if digit_accounts[source] < transition + round(fee_value,2):
            return accounts

        digit_accounts[source] = digit_accounts[source] - transition - round(fee_value,2)
        digit_accounts[destination] = digit_accounts[destination] + transition
        for i in range(len(digit_accounts)):
            if round(digit_accounts[i],2) % 1 == 0:
                accounts[i] = str('%.1f' % float( digit_accounts[i]))    
            else:
                accounts[i] = str('%.2f' % float( digit_accounts[i]))
            if accounts[i] == '-0.0':
                accounts[i] = '0.0'

        return accounts

    else:
        digit_accounts[source] = digit_accounts[source] - transition
        digit_accounts[destination] = digit_accounts[destination] + transition
        for i in range(len(digit_accounts)):
            if digit_accounts[i] % 1 == 0:
                accounts[i] = str('%.1f' % float( digit_accounts[i]))
            else:
                accounts[i] = str('%.2f' % float( digit_accounts[i]))

        return accounts
    

def problem9(num):
    num=list(range(num))
    num= [i+1 for i in num]
    new_num=[]
    count = 0
    while count < len(num)*9 :
        new_num.extend(num)
        count += 1
    
    while len(num)!=1:
        num.remove(new_num[8])
        eliminated=new_num[8]
    
        for i in range(0,9):
            new_num.pop(0)

        while eliminated in new_num:
            new_num.remove(eliminated)
    
    return num[0]

def problem10(string_list):
    for i in range(len(string_list)):
        for j in range(i+1,len(string_list)):
            if string_list[i] == string_list[j]:
                return string_list[i]

