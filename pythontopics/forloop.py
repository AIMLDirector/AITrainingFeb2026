list1= ["apple", "banana", "cherry"]
for i in list1:
    print(i)
for fruit in list1:
    print(fruit)

name = "John"  # str

for i in name:
    print(i)

count = 0
for i in name:
    if i in "aeiou":
        print(f"{i} is a vowel")
        count += 1
    else:
        print(f"{i} is a consonant")

print(f"Total number of vowels in the name: {name} is : {count}")
    
companyinfo = {"name": "Google", "location": "Mountain View", "employees": 100000}

for i in companyinfo:
    print(i)  # prints the keys of the dictionary

for value in companyinfo.values():
    print(value)  # prints the values of the dictionary


for k,v in companyinfo.items():
   print(v)

list2 = [1, 2, 3, 4, 5]
sqr = []
for i in list2:
    print(i)
    sqr.append(i**2)

print(sqr)

evenlist = []
oddlist = []
for i in list2:
    if i % 2 == 0:
        print(f"{i} is even")
        evenlist.append(i)
    else:
        print(f"{i} is odd")
        oddlist.append(i)

print(f"Even numbers: {evenlist}")
print(f"Odd numbers: {oddlist}")

folder - 10 files ( txt, pdf, docx, pptx, csv)
pdf files -- list ( pdf file names)
print the list 

for and if and list 