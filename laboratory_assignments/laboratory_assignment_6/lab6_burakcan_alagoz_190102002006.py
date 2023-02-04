#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from random import randint

my_name = "Burak Can Alagoz"
my_id = "190102002006"
my_email = "b.alagoz2019@gtu.edu.tr"


#Problem 0 - Getter & Setter [0 pts]
def problem0():
    '''Doctests
    >>> A = problem0()
    >>> ainst = A(3)
    >>> ainst.get_value()
    3
    >>> A = problem0()
    >>> ainst = A(1)
    >>> ainst.get_value()
    1
    >>> A = problem0()
    >>> ainst = A(-4)
    >>> ainst.get_value()
    -4
    >>> ainst.set_value(5)
    >>> ainst.get_value()
    5
    '''
    class p0:   
        def __init__(self, x):
            self.a = x

        def get_value(self):
            return self.a

        def set_value(self, x):
            self.a = x

    return p0


#Problem 1 - Integer only Getter & Setter [10 pts]
def problem1():
    '''Doctests
    >>> A = problem1()
    >>> ainst = A(3.5)
    >>> ainst.get_value()
    0
    >>> A = problem1()
    >>> ainst = A([1])
    >>> ainst.get_value()
    0
    >>> A = problem1()
    >>> ainst = A(None) # Creating an instance with None as parameter
    >>> ainst.get_value()
    0
    >>> A = problem1()
    >>> ainst = A(-4)
    >>> ainst.get_value()
    -4
    >>> ainst.set_value(7.6)
    >>> ainst.get_value()
    -4
    >>> ainst.set_value(3)
    >>> ainst.get_value()
    3
    '''
    class p1:
        def __init__(self,x):
            if type(x) == int:
                self.a = x
            else:
                self.a = 0

        def get_value(self):
            return self.a

        def set_value(self, x):
            if type(x)!= int:
                pass
            else:
                self.a=x
            
    return p1

#Problem 2 - Rectangle [10 pts]
def problem2():
    '''Doctests
    >>> A = problem2()
    >>> ainst = A(3, 5)
    >>> ainst.get_area()
    15
    >>> ainst.get_perimeter()
    16
    '''
    class p1:
        def __init__(self,x,y):
            self.a = x
            self.b = y

        def get_area(self):
            return self.a * self.b

        def get_perimeter(self):
            return (2 * self.a) +(2 * self.b)

    return p1

#Problem 3 - Grades [12 pts]
def problem3():
    '''Doctests
    >>> A = problem3()
    >>> ainst = A()
    >>> ainst.get_min()
    0.0
    >>> ainst.get_max()
    0.0
    >>> ainst.get_mean()
    0.0
    >>> ainst.get_median()
    0.0
    >>> ainst.add_grade(3)
    >>> ainst.add_grade(5)
    >>> ainst.get_min()
    3.0
    >>> ainst.get_max()
    5.0
    >>> ainst.get_mean()
    4.0
    >>> ainst.get_median()
    4.0
    >>> ainst.add_grade(10)
    >>> ainst.get_min()
    3.0
    >>> ainst.get_max()
    10.0
    >>> ainst.get_mean()
    6.0
    >>> ainst.get_median()
    5.0
    >>> ainst.remove_grade(15)
    >>> ainst.remove_grade(10)
    >>> ainst.get_min()
    3.0
    >>> ainst.get_max()
    5.0
    >>> ainst.get_mean()
    4.0
    >>> ainst.get_median()
    4.0
    '''
    class Grades:
        def __init__(self):
            self.internalList = []
            self.max = max
            self.min = min

        #that will add the given grade to the internal list.
        def add_grade(self,x): 
            self.internalList.append(x)

        #that will return the grade from the internal list if it exists, if it does not exist, it will just ignore it.
        def remove_grade(self,x):
            try:
                self.internalList.remove(x)
            except ValueError:
                pass    

        #return the minimum grade.
        def get_min(self):
            return float(min(self.internalList)) if len(self.internalList)>0 else 0.0

        #return the maximum grade.
        def get_max(self):
            return float(max(self.internalList)) if len(self.internalList)>0 else 0.0

        #return the mean (average) grade.
        def get_mean(self):
            if len(self.internalList)<1:
                return 0.0

            sum = 0
            for i in self.internalList:
                sum += i
            return float(sum / len(self.internalList))

        #return the median grade. If the number of grades are even, returns the average of the middle two grades (assuming the grades are sorted).
        def get_median(self):
            if len(self.internalList)<1:
                return 0.0
            if len(self.internalList)%2==0:
                return (self.internalList[int(len(self.internalList)/2)]+self.internalList[int(len(self.internalList)/2)-1])/2
            else:
                return float(self.internalList[int(len(self.internalList)/2)])

    return Grades              


#Problem 4 - Movie [14 pts]
def problem4():
    class Movie:
        def __init__(self,movie_name,director,year,rating = 0.0,length = 0):
            self.dict = {"movie_name":movie_name , "director":director ,  "year":year}
            
            if  0.0 <= rating <= 10.0:
                self.dict["rating"] = rating
            else:
                self.dict["rating"] = 0.0

            if 0 <= length <= 500:
                self.dict["length"] = length
            else:
                self.dict["length"] = 0

        def get_movie_name(self):
            return self.dict["movie_name"]

        def get_director(self):
            return self.dict["director"]

        def get_year(self):
            return self.dict["year"]

        def get_rating(self):
            return self.dict["rating"] 

        def get_length(self):
            return self.dict["length"]

        def set_rating(self,x):
            if  0.0 <= x <= 10.0:
                self.dict["rating"] = x
            else:
                pass
        
        def set_length(self,x):
            if 0 <= x <= 500:
                self.dict["length"] = x
            else:
                pass

    return Movie            

#Problem 5 - Movie Catalog [16 pts]
def problem5():
    '''Doctests
    >>> A = problem5()
    >>> ainst = A('movies.txt')
    >>> ainst.add_movie('The Usual Suspects', 'Bryan Singer', 1995, 8.5, 106)
    >>> ainst.get_oldest()
    'The Godfather'
    >>> ainst.get_highest_ranking()
    'The Shawshank Redemption'
    >>> ainst.get_lowest_ranking()
    'The Usual Suspects'
    >>> ainst.get_by_director('Nuri Bilge Ceylan')
    []
    >>> ainst.get_by_director('Francis Ford Coppola')
    ['The Godfather', 'The Godfather: Part II']
    '''
    class MovieCatalog:
        def __init__(self,filename) -> None:
            file = open(filename, 'r')
            self.lst = []

            for element in file:
                new_element = element.strip("\n").split(",")
                self.lst.append(problem4()(new_element[0], new_element[1], int(new_element[2]), float(new_element[3]), int(new_element[4])))

            file.close

        def add_movie(self,movie_name,director,year,rating=0.0,length=0):
            if problem4()(movie_name, director, year, rating, length) not in self.lst:
                self.lst.append(problem4()(movie_name, director, year, rating, length))

        def remove_movie(self, movie_name):
            for film in self.lst:
                if film["movie_name"]==movie_name:
                    self.lst.remove(film)

        def get_oldest(self): 
            oldest = self.lst[0]
            for i in self.lst:
                if i.dict["year"] < oldest.dict["year"]:
                    oldest=i
                    
            return oldest.dict["movie_name"]

        def get_lowest_ranking(self):
            lowest = self.lst[0]
            for i in self.lst:
                if i.dict["rating"] < lowest.dict["rating"]:
                    lowest=i
            return lowest.dict["movie_name"]
        
        def get_highest_ranking(self):
            highest = self.lst[0]
            for i in self.lst:
                if i.dict["rating"] > highest.dict["rating"]:
                    highest=i
            return highest.dict["movie_name"]
        
        def get_by_director(self, director):
            directors_movies = []
            for i in self.lst:
                if i.dict["director"]== director:
                    directors_movies.append(i.dict["movie_name"])
            return directors_movies

    return MovieCatalog



#Problem 6 - Node [12 pts]
def problem6():
    '''Doctests
    >>> N = problem6()
    >>> ninst1 = N(3, 4, 5)
    >>> ninst1.get_node()
    (3, 4, 5)
    >>> res = ninst1.get_distance()
    >>> import math
    >>> math.isclose(res, 7.07, rel_tol=1e-2)
    True
    >>> print(ninst1)
    <3, 4, 5>
    >>> ninst2 = N(-2, 3, 5)
    >>> ninst3 = ninst1 + ninst2
    >>> print(ninst3) 
    <1, 7, 10>
    >>> ninst2 > ninst1
    False
    >>> ninst2 >= ninst1
    False
    >>> ninst2 < ninst1
    True
    >>> ninst2 <= ninst1
    True
    >>> ninst2 == ninst1
    False
    >>> ninst2 = N(-3, 4, 5)
    >>> ninst2 == ninst1
    False
    >>> ninst2 = N(3, 4, 5)
    >>> ninst2 == ninst1
    True
    >>> ninst2 is ninst1
    False
    '''
    class Node:
        def __init__(self,x,y,z) -> None:
            self.x = x
            self.y = y
            self.z = z

        def get_node(self):
            return (self.x,self.y,self.z)

        def get_distance(self):
            return ((self.x**2)+(self.y**2)+(self.z**2))**0.5

        def __add__(self,second):
            return problem6()(self.x + second.x , self.y + second.y , self.z + second.z)

        def __str__(self):
            return "<"+str(self.x)+", "+str(self.y)+", "+str(self.z)+">" 

        def __gt__(self,second):
            return self.get_distance() > second.get_distance()

        def __ge__(self,second):
            return self.get_distance() >= second.get_distance()

        def __lt__(self,second):
            return self.get_distance() < second.get_distance()

        def __le__(self,second):
            return self.get_distance() <= second.get_distance()

        def __eq__(self,second):
            return (self.x, self.y, self.z) == (second.x, second.y, second.z)

    return Node



#Problem 7 - Node Cloud [14 pts]
def problem7():
    '''Doctests
    >>> A = problem7()
    >>> ainst = A(5)
    >>> nodes = ainst.get_nodes()
    >>> len(nodes)
    5
    >>> isinstance(nodes, list)
    True
    >>> isinstance(nodes[0], tuple)
    True
    >>> ainst.add_node(21, 21, 21)
    >>> nodes = ainst.get_nodes()
    >>> len(nodes)
    6
    >>> ainst.get_outermost()
    (21, 21, 21)
    >>> s = ainst.get_sum()
    >>> len(s.get_node())
    3
    '''
    class NodeCloud:
        def __init__(self,n) -> None:
            if n>0:
                self.number = n
                self.coordinates = []
                for i in range(n):
                    self.coordinates.append(problem6()(randint(-20, 20), randint(-20,20), randint(-20,20)))
        
        def get_nodes(self):
            nodes=[]
            for i in self.coordinates:
                nodes.append((i.x, i.y, i.z))
            return nodes
        
        def get_outermost(self):
            furthest = self.coordinates[0]
            for i in self.coordinates:
                if float((i.x**2+i.y**2+i.z**2)**0.5) > (furthest.x**2+furthest.y**2+furthest.z**2)**0.5:
                    furthest=i
                    
            return furthest.x, furthest.y, furthest.z
        
        def add_node(self, x, y, z):
            self.coordinates.append(problem6()(x, y, z))
        
        def get_sum(self):
            sum = problem6()(0,0,0)
            for i in self.coordinates:
                sum.x += i.x
                sum.y += i.y
                sum.z += i.z 
            return sum

    return NodeCloud




#Problem 8 - Encoder [12 pts]
def problem8():
    '''Doctests
    >>> A = problem8()
    >>> ainst = A("test")
    >>> print(ainst)
    test
    >>> ainst.morse()
    ['-', '.', '...', '-']
    >>> ainst.binary()
    '1110100110010111100111110100'
    >>> ainst.hex()
    '74657374'
    >>> ainst = A("çELık-!")
    >>> print(ainst)
    ELk
    >>> ainst.morse()
    ['.', '.-..', '-.-']
    >>> ainst.binary()
    '100010110011001101011'
    >>> ainst.hex()
    '454c6b'
    '''
    class Encoder:
        def __init__(self,x) -> None:
            self.text = ""

            for char in x:
                if 48 <= ord(char) <= 57 or 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
                    self.text += char

        def __str__(self):
            return self.text

        def morse(self):
            morse_version = []
            morse_code_dict = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'} 
            for char in self.text:
                morse_version.append(morse_code_dict[char.upper()])

            return morse_version   


        def binary(self):
            return ''.join(format(ord(x), 'b') for x in self.text)

        def hex(self):
            hex_version = "" 
            for c in self.text:
                hex_version += "{:x}".format(ord(c)) 
            return hex_version

    return Encoder

        
# if __name__ == "__main__":

#     #python -m doctest -v lab6_burakcan_alagoz_190102002006.py
#     import doctest
#     doctest.testmod()

#     print("Completed all doctests.")

