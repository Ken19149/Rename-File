import os

path = input("File location: ")
file_type = "." + input("File format: ")
file_name = input("New file name: ")

i = 0

for file in os.listdir(path):
    if file_type in file:
        i += 1
        os.rename(path + "\\" + file, path + "\\" + file_name + "_" + str(i) + file_type)
