# i = 1
# while i <= 5: # condition with exit statement or exit option 
#     print(i)
#     i += 1

# # while <condition>:
# #   <action>

# j  = 1
# while True:   # virus code/hackers will use while loop 
#     print(j)
#     if j == 5:
#             break
#     j+= 1


import requests
success = False

while 
    response = requests.get('https://api.github.com/events1')
    if response.status_code == 200:
        print("Data fetched successfully!")
        success = True
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}. Retrying...")


role = "admin"
username = "kumar"

while username != "kumar" or role != "admin":
    print("Access denied. Please enter correct username and role.")
    username = input("Enter username: ")
    role = input("Enter role: ")
print("Welcome, admin kumar!")


correct_username = "kumar"
correct_password = "password123"

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login successful!")

        break
    else:
        attempts += 1
        print(f"Invalid credentials. Attempt {attempts} of {max_attempts}.")

