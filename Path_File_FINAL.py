import os

#prompt user to input valid path
print("please input path name")
path_name = input()

#program will let user know path is valid or not
is_path = os.path.exists(path_name)
if (is_path == False):
    print("please input valid path")

else:
    print("please choose a file name. Example: text.txt")
    file_name = input()
    print("Please input your name")
    name = input()
    print("please input your address")
    address = input()
    print("please input your telephone number")
    number = input()

    with open(os.path.join(path_name,file_name),"w") as file:
        file.write(name + ", ")
        file.write(address + ", ")
        file.write(number)
        

    with open(os.path.join(path_name,file_name),"r") as file:
        file_contents = file.read()
        print('You input the following information into your chosen .txt file: ', file_contents)
        print('Good-bye')
