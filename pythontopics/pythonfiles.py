import os
  # os module we used in build  listdir()
# filelist =[]
# # l1= os.listdir()  # list of files and directories in the current working directory
# # print(l1)
# for i in os.listdir():
#     if i.endswith(".py"):
#         filelist.append(i)


# print(filelist)

# pythonfiles = []
# nonpythonfiles = []

# for a in os.listdir():
#     if a.endswith(".py"):    # endwith and startswith are used to check the file extension and file name respectively
#         pythonfiles.append(a)
#     else:
#         nonpythonfiles.append(a)

# print("Python files: ", pythonfiles)
# print("Non-Python files: ", nonpythonfiles)

# pyfiles = [i for i in os.listdir() if i.endswith(".py")]
# print("Python files using list comprehension: ", pyfiles)




for a in os.listdir():
    print(a)
