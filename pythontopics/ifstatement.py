a = 1
b = 2
c = 3

if a < b:
    print("a is less than b")


if a < b :
    print("a is less than b")
else:
    print("a is greater than or equal to b")

if a < b and a < c:
    print("a is less than b and c")
elif b >c and b > a:
    print("b is greater than a and c")
else:
    print("c is greater than a and b")


Age = 20
Salary = 50000
if Age > 18 and Salary > 30000:
    print("You are eligible for the loan")
else:
    print("You are not eligible for the loan")

username = "kumar"
role = "admin"
if username == "kumar" and role == "admin":
    print("Welcome, admin kumar!")
else:
    print("Access denied.")

filenames = [ "report.docx", "data.csv", "presentation.pptx", "notes.txt","report2.docx" ]

for i in filenames:
    if i.endswith(".docx") and i.startswith("report"):  
        print(f"{i} is a Word document.")

for i in filenames:
    if i.endswith(".docx"):  
        print(f"{i} is a Word document.")

doclist = []
for i in filenames:
    if i.endswith(".docx"):
        doclist.append(i)

print(doclist)

sentence = "Python is a great programming language."
if "Python" in sentence:
    print("The word 'Python' is present in the sentence.")

words = sentence.split()
print(words)
for i in words:
    if i.startswith("p") or i.startswith("P"):
        print(f"{i} starts with 'p' or 'P'.")

