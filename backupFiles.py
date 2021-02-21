import os
import shutil
path = input("Enter Name Of the Directory to be Moved")
destination = "/Python Programs/text2/"
listOfFiles = os.listdir(path)
for file in listOfFiles:
    shutil.move((path+file),destination)