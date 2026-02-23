# try:
#     a = int(input("Enter a number: "))
#     print(f"You entered: {a}")
# except ValueError:
#     print("Invalid input. Please enter a valid integer.")


# try:
#     a = int(input("Enter a number: "))
#     print(f"You entered: {a}")
# except Exception as e :
#     print("Error code:", e, "Invalid input. Please enter a valid integer.")

# try:
#     with open("non_existent_file.txt") as f:
#         content = f.read()
#         print(content)
# except FileNotFoundError:
#     print("The file does not exist.")
# except Exception as e:
#     print("An error occurred:", e)


# def check_age(age):
#     if age < 0:
#         raise ValueError("Age cannot be negative.")
#     elif age < 18:
#         return "You are a minor."
#     else:
#         return "You are an adult."

# try:
#     age_input = int(input("Enter your age: "))
#     result = check_age(age_input)
#     print(result)
# except ValueError as ve:
#     print("ValueError:", ve, type(ve))


try:
    result = 10/0
except Exception as e:
    print("An error occurred:", e, type(e)) 


class CustomError(Exception):
    pass    

try:
    a = b+c 
    print(a)
except CustomError as ce:
    print("Caught a CustomError:", ce, type(ce))
