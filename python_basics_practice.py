'''

DS2000 Spring 2022
Benjamin Teixeira
    
Filename: sarker_wip.py
    
Description:
    
'''
# importing libraries, creating first lists
import random as rnd
lst = [1,2,3,5]
lst_2 = [15,"Hello", True, 4.3]

# accessing list members
print(lst[0],"A")
print(lst[3],"B")
print(len(lst),"C")
print(lst[-1],"D")
print(lst[1:3],"E")
print(lst[-2:],"F")
print(lst[:-2],"G")
print(lst[-1::-1],"h")

# Generating lists
lst_3 = []
for x in range(0,10):
    lst_3.append(x)
    
print(lst_3)

# list comprehension
lst_4 = [x for x in range(0,20)]
print(lst_4)

# while loop
i = 0

while i < len(lst_4):
    print(lst_4)
    i += 1
    
print(i)

# list with numbers divisible by 5
lst_5 = [x for x in range(0,100) if x % 5 == 0]
print(lst_5)

# add lists together
lst_6 = lst_4 + lst_5
print(lst_6)

# extend lists
lst_6.extend(lst_4)
lst_6.extend(lst_5)
print(lst_6)

print("1/15/23")

# iteraing over a list and seeing if certain values
# exist in it
lst_7 = [x for x in range(0,100)]
for i in range(0,len(lst_7)):
    print(lst_7[i])
    print("meatball meatball meatball")
    
# iterating over a list properly in Python
for i in lst_7:
    print(i)

# see if certain numbers are in lst_7
print(bool(25 in lst_7))
print(bool(-45 in lst_7))

# sorting a list to reverse it
lst_7.sort(reverse = True)
print(lst_7)

# reverse a list without sorting
lst_8 = [1,2,3,4,5]
lst_8.reverse()
print(lst_8)

# sorting: custom sorting functions. reversing: only reversing 
# generating a random list
lst_9 = [rnd.randint(0,10) for x in range(0,50)]
print(lst_9)

# handling lists; generating a list from a list of random numbers 
# UNPROVEN
lst_10 = [rnd.randint(0,100) for x in range(0,10)]
lst_11 = [lst_10 for x in range(0,10) if lst_10[x] % 3 == 0]
print(lst_11)
print(len(lst_11))

# sets: a collection of well-defined distinct objects
# removing duplicates through the set data type
lst_12 = [1,2,2,2,3,4,5,5,6]
lst_13 = list(set(lst_12))
print(lst_13)

# union and intersection of sets; everything from both sets
# creating sets
set_1 = {"Apple", "Orange", "Banana"}
set_2 = {"Pineapple", "Grape", "Banana"}

# printing unique values from both sets
print(set_1 | set_2)

# printing only common vaues from both sets
print(set_1 & set_2)

# creating null sets & dictionaries
null_set_1 = set({})
null_set_2 = {}
print(null_set_1,",", null_set_2)

# dictionaries: a collection of several elements as key:value pairs
# generally use numbers or strings as keys, not bool
# keys must be unique
dict_1 = {"key1":"value1","key2":"value2",
          "key3":{"subkey":"value3"}}
print(dict_1)

# Accessing and Setting Values in a Dictionary
print(dict_1["key2"])

# create new dictionary value
dict_1["key2"] = "My new value"
print(dict_1)

# define a blank dictionary and assign values to it
dict_3 = {} 
dict_3["key1"] = "Value4"
print(dict_3["key1"])

# iterating over a dictionary's itms looping with (k, v) values & 
# formatting into a new order
for k, v in dict_1.items():
    print("{} - {}".format(k, v))
    
# generating random list... 
lst_14 = [rnd.randint(0,30) for x in range(0,100)]
print(lst_14)
print("Random List Length:",len(lst_14))

#...creating unique valued list with duplicates removed
print(list(dict.fromkeys(lst_14).keys()))
print("Unique Valued List Length:", 
      len(list(dict.fromkeys(lst_14).keys())))

# deleting a key:value pairing from a dictionary
# can delete a specific index from a list as well
del dict_1["key3"]
print(dict_1)

# dictionary comprehension using squared numbers
lst_15 = [x for x in range(0,10)]
dict_4 = {x: x**2 for x in lst_15}
print(dict_4)

# generating a dictionary using the dict function
dict_5 = dict([('Ben',100),('Benny',200),('Benn',300)])
dict_6 = dict(Ben = 100, Benny = 200, Benn = 300, Benno = 400)
print(dict_5)
print(dict_6)

# tuples
tuple_1 = 1,2,3
print(tuple_1)

# creating a tuple with different cardinalities (immutable)
tuple_2 = ()
tuple_2 = "Hello There","General Kenobi"
print(tuple_2)

# unpacking tuples; getting values in tuples in different variables
tuple_3 = "Big","Ben"
big, ben = tuple_3
print(tuple_3)

# strings
string1 = "Hello World"
print(string1)

# Accessing Strings
str2 = "Hello World!"
print(str2[0],str2[4],str2[1],"s Mad",str2[-1])

# String Slices
str3 = "Hello World! I am learning data wrangling!"
print(str3[2:10])
print(str3[-15:])
print(str3[-10:-5])

# string functions
print(len(str3))
print(str3.upper())
print(str3.lower())
print(str3.find("data"))
print(str3.replace("am","love"))

# Split and Join
str4 = "Name, Age, Sex, Job"
lst_16 = str4.split(",")
print(lst_16)
print(" |".join(lst_16))




    












