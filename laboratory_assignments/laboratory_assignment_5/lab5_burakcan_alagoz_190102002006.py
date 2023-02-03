my_name = "Burak Can Alagoz"
my_id = "190102002006"
my_email = "b.alagoz2019@gtu.edu.tr"


#Problem 1 - nth frequency [5 pts]
def problem1(num_list,n):
    frequency = []
    for num in num_list:
        if num_list.count(num) == n and not num in frequency:
            frequency.append(num) 
            
    return frequency


#Problem 2 - Median grade [7 pts]
def problem2(class_grades):
    grades = list(class_grades.values())
    grades.sort()
    #grades = [10,20,30,42.5,51.25,60,70,80]

    if len(grades) == 0:
        return 0
    if len(grades) % 2 != 0:
        return grades[int((len(grades))/2)]
    else:
        if (float((grades[int(len(grades)/2)] + grades[int((len(grades)/2)-1)]))/2 ) % 2 == 0:
            return (grades[int(len(grades)/2)] + grades[int((len(grades)/2)-1)])/2
        else:
            return float((grades[int(len(grades)/2)] + grades[int((len(grades)/2)-1)]))/2  



#Problem 3 - Read Transcript [13 pts]
def problem3(filename):
    try:
        file = open(filename, 'r')
    except :
        return []    

    content_list = []

    for element in file:
        new_element = element.strip().split(",")
        content_list.append({"name":new_element[0], "credit":int(new_element[1]), "term":int(new_element[2]), "grade":new_element[3].strip()})
        if content_list[-1]["grade"]=="": #If the given course does not have a grade, enter NA
            content_list[-1]["grade"]="NA"

    file.close()

    return content_list

#Problem 4 - Term GPA [14 pts]
def problem4(dictionary_list,term_number):
    grades = {"AA":4.0, "BA":3.5, "BB":3.0, "CB":2.5, "CC":2.0, "DC":1.5, "DD":1.0, "FF":0.0, "NA":None}
    point_sum = 0
    credit_sum = 0

    for elm in dictionary_list:
        if elm["grade"] != "NA" and elm["term"] == term_number :
            credit_sum += elm["credit"] 
            point_sum += elm["credit"] * grades[elm["grade"]]

    if credit_sum != 0:
        return (point_sum/credit_sum)*100/100
    else: 
        return 0


#test funcktion
#should find and return the number of 1's up to (including) the given number starting from 0.
#def ffunc(n):
#    return str(list(range(n+1))).count("1")



#Problem 5 - Black Box Testing [16 pts]
def problem5(func,num):
    return func(num) == str(list(range(num+1))).count("1")



#Problem 6 - Combinations [10 pts]
def problem6(string):
    string = string.lower()
    if len(string) == 1:
        return [string]
    else:   
        perms = []
        for i in range(len(string)):
            for perm in problem6(string[:i] + string[i+1:]):
                perms.append(string[i] + perm)
            perms.append(string[i])  

    perms.sort() 
    unique_perms = list(set(perms))
    unique_perms.sort()       
    return unique_perms


#Problem 7 - Anagrams [5 pts]
def problem7(string1,filename): #first finish problem6
    permutations = problem6(string1)
    file = open(filename, 'r')
    valid_words = []

    for word in file:
        for elm in permutations:
            if word.strip("\n") == elm:
                valid_words.append(elm)
    file.close()
    return valid_words

#Problem 8 - Sub-matrix [14 pts]
def problem8(matrix, sub_matrix): 

    len_sub_matrix = len(sub_matrix)

    curr = 0
    for x in sub_matrix:
        for y in matrix:
            if set(x).issubset(y):
                curr += 1
                break

    return True if len_sub_matrix == curr else False
            
    

#Problem 9 - Compression [7 pts]
def problem9(string):
    compressed = ""
    temp = ""
    count = 1

    for char in string:
        if char != temp:
            if count > 1:
                compressed += str(count)
            compressed += char    
            count = 1
        else:
            count += 1
        temp = char

    if count > 1:
        compressed += str(count)       

    compression_rate = ((len(string)-len(compressed))*100)/len(string)

    return compressed,int(compression_rate)

 
#Problem 10 - Missing Number [9 pts]
def problem10(number_list):
    number_list.sort()
    full_list = list(range(number_list[0],number_list[-1]+1))

    if full_list == number_list:
        return number_list[-1]+1

    for i in range(len(number_list)):
        if number_list[i] != full_list[i] :
            return full_list[i]




if __name__ == "__main__":


    print("Running problem 8")
    print(problem8([[1, 2], [3, 4]], [[1], [4]]))
