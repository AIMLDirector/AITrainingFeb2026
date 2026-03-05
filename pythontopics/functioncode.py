def fcode():
    print("This is a function")

fcode()

def fcode1(name:str):
    print(f"Hello, {name}!")

fcode1("kumar")


def fcode2(num1:int = 5, num2:int = 20) -> int:
    return num1 + num2

result = fcode2(5, 10)

print(f"The sum of 5 and 10 is: {result}")

result1 = fcode2(30,50)
print(result1)

list1 = [1, 2, 3, 4, 5]
def sqrlist(l1):
    sqr = []
    for i in l1:
        sqr.append(i**2)
    return sqr


sqrresult = sqrlist(list1)   
print(sqrresult)


