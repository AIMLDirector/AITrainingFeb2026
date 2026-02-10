import os
from datetime import datetime
import time

start_time = datetime.now()
print("Start time: ", start_time)
cmd1 = os.system("df -h")
cmd2 = os.system("ls -l")
time.sleep(10)
end_time = datetime.now()   
print("End time: ", end_time)
print("Time taken to execute the commands: ", end_time - start_time)    