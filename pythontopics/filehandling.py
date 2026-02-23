
# a = open("input_output.txt")
# print(a.read())
# a.close()


# with open("input_output1.txt") as f:
#     print(f.read())
#     f.close()

# import os

# file_path = "input_output1.txt"
# if os.path.exists(file_path):
#     with open(file_path) as f:
#         print(f.read())
#      f.close()
# else:
#     print(f"The file {file_path} does not exist.")



# def read_file(file1: str) -> str:
#     try:
#         with open(file1) as f:
#             content = f.read()
#             print(content)
#         f.close()
#     except FileNotFoundError:
#         print(f"The file {file1} does not exist.")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#     finally:
#         print("Finished attempting to read the file.")
       

    
# read_file("input_output.txt")

# def filter_critical_messages(input_file: str, output_file: str):
#     try:
#         with open(input_file) as infile, open(output_file, 'w') as outfile:
#             for line in infile:
#                 if "CRITICAL" in line:
#                     outfile.write(line)
#                 print(outfile)
#     except FileNotFoundError:
#         print(f"The file {input_file} does not exist.")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#     finally:
#         print("Finished processing the log file.")


# filter_critical_messages("/Users/premkumargontrand/AITrainingFeb2026/pythontopics/data/app.log", "/Users/premkumargontrand/AITrainingFeb2026/pythontopics/data/critical_messages.log")


# from datetime import datetime

# def log_messages(message):
#     with open("cdweb.log", "a") as log_file:
#         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         log_file.write(f"{timestamp} - {message}\n")


# log_messages("info: Application started")

# date:<info|critical|warning|error> : message content


import csv

# with open("data.csv", "w", newline="") as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["Name", "Age", "City"])
#     writer.writerow(["Alice", 30, "New York"])
#     writer.writerow(["Bob", 25, "Los Angeles"])



# with open("data.csv", "r") as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         print(row)

# json file dump is to write the data and load is to read the data from json file

import json

data = {name: "Alice", age: 30, city: "New York"}

with open("data.json", "w") as jsonfile:
    json.dump(data, jsonfile)   



with open("data.json", "r") as jsonfile:
    data_loaded = json.load(jsonfile)
    print(data_loaded)


# text, csv, json , binary, library , xml, yaml, pdf



