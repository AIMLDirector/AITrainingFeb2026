
# a = 1 
# b = 2.5
# c = "Hello, World!"

# print(type(a))
# print(type(b))
# print(type(c))
# print("The value of a first time ", a)

# def func1():
#     d = 4
#     print("The value of d inside func1 before modification ", d)
#     print("The value of a inside func1 is ", a)

# print("The value of a second time ", a)
# #print("The value of d is ", d)

l2 = [1, 2, 3, 4, 5, 2.5, 'sam',2,3]  # single dimension array 
l1 = []
#  adding data to this list will be done by 3 ways append , insert , extend
l2.append(5)
print(l2)
l2.insert(2, "kumar")
print(l2)
l3 = [10, 20, 30]
l2.extend(l3)
print(l2)
# removing the data in the list will be done by 3 ways remove, pop, clear
l2.remove(2.5)
print(l2)
l2.pop()  # removes the last element
print(l2)
l3.clear()  # removes all the elements
print(l3)
#sorting the data in the list
l4 = [5, 2, 8, 1, 4]
l4.sort()
print(l4)    # will give error as the list contains different data types
l4.sort(reverse=True) # will give error as the list contains different data types
print(l4)

# accessing the elements in the list
print(l2[0])  # first element  index from left to right 0 to n-1   , right to left -1 to -n
print(l2[-1])  # last element
print(l2[2:5])  # elements from index 2 to 4

a = l2.count(3)
print(a)  # count the number of occurrences of 3 in the list