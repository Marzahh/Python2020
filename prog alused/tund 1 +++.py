LIST is something in []

a = [3,10,-1]
a.append[1,"hello"] add anything to the end of the list ~~~ a = [3,10,-1,1,"hello"]
a.append ([1,"hello"]) add lis to the list so   ~~~ a = [3,10,-1,1,"hello",[1,"hello"]]
print(a,[0]) print from the list a 0 character ~~~ 3
a[0]=100 assigne new value to the first character of the list a ~~~ a = [100,10,-1,1,"hello",[1,"hello"]]


multiplication of list zeros= [0]*5 = [0,0,0,0,0]
adding lisits  letters= ["a","b"] , zeros+letters [0,0,0,0,0,"a","b"]
range(20)= [0.....19]
len or lengh   chars=["Hello World"], len(chars) = 11 (we count each character and space)
slicing    letters=[a,b,c,d,e] print letters[0;3] aka from 0 to 3-1 so a,b,c
INDEX   courses=["History","Math","Physic"]    print(courses.index=("Math"))   prints 1 (position in the list)
check if it is in the list   print ("Math" in courses)   prints True (or false)
split list   s=[1,2,3,4,5] print (s.split(","))   ["1", "2", "3"...] you can split text to by space or capital letters

TUPLETS ()
you cant modify them
you can not change a value like in a list
instead of [] they have () and function like a list with exception that you cant modify them and append

SETS {}
characters inside do not have a set order so you cant find which on is on a which place
they have no repeating values
they are used to through away dublicats
to check  if it is in    print ("Math" in courses)   prints True (or false)
CREATE empty_set=set()   NOT{} #this is a dictionary

DICTIONARY {}
student{"name":"John", "age":"25"} first one is key, second value
print(student["name"])    John
add key and value to the dictionsry(adds to the end) student["phone"]="55640285"
show amount of keys print (len("student"))     3
print all keys or all values   print(student.keys()) or print(student.values())


import random
random.randint(1,6) numbers from 1 to 6
== <= >= > < !=
else elif
input default is string
7//2= 3 (täisarvuni)
7/2 = 3,4 (normal)
7%2= 1 (jääk)
6**(2)= 6 astmes 2

