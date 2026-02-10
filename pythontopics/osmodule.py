import os

print(os.name)
print(os.getcwd())  # current working directory

print(os.chdir("/Users/premkumargontrand/AITrainingFeb2026/Gitcommand"))  # change the current working directory
print(os.getcwd())  # current working directory
print(os.listdir())  # list of files and directories in the current working directory


a = os.system("df -h")  # execute the command in the terminal and return the output