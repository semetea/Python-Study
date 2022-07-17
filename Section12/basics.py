import time, os
import pandas

while True :
    if os.path.exists("files/vegetables.txt") :
        with open("files/vegetables.txt") as file:
            print(file.read())
            time.sleep(10)
    else :
        print("File does not exist")
    time.sleep(10)