
# set is a collection which is unordered, unchangeable*, and unindexed. No duplicate values are allowed.
s1 = {"apple", "banana", "cherry"}
print(s1)

list1 =[1,2,3,1,2,3,4,3,5,6,7,8,9,10] 


# list1 = list(set(list1))  # will remove the duplicate values and will give a list of unique values
# print(list1)
# print(list1)
# s2 = set(list1)
# print(s2)  # will remove the duplicate values and will give a set of unique values
# list1 = list(s2)
# print(list1)  # will give a list of unique values

list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)

print("list2 value:", list2)  # will give a list of unique values

print(list2[3:8])