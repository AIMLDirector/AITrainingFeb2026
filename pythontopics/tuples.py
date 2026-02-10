# tuples items are ordered, unchangeable, and allow duplicate values.

tuple1 = ("apple", "banana", "cherry")  # index value ( 0,1,2)   ( -3,-2,-1) - Static value 
print(tuple1)
tuple2 = list(tuple1)
print(tuple2)
tuple2.append("orange")
print(tuple2)
tuple1 = tuple(tuple2)
print(tuple1)
print(tuple1[0])  # accessing the first element

# for i in tuple1:
#     print(i)

 
for i in range(len(tuple1)):
    print(tuple1[i])

set1 = set(tuple1)  
print(set1)  # will remove the duplicate values and will give a set of unique values

# list = []  list of vallue
# tuples = ()  list of value but unchangeable
# set = {}  list of unique values
# dictionary = {}  list of key value pairs
# function or class or method  = def func1() or class testclass1()
# converting data from one format to another format is called typecasting or type conversion
# list = tuple() set()    etc

# print(), input(), range(), len(), type(), int(), float(), str()  are some of the built-in functions in python 
