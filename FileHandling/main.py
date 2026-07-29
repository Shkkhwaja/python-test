from pathlib import Path
import os


def createFile():

    try:
        name = input("Enter file name : ")
        path = Path(name)

        if not path.exists():
            with open(path,"w") as f:
                cont = input("Enter your content : ")
                f.write(cont)
            print("file created !!")
        else:
            print("File already exists")
    except Exception as err:
        print("File error ",err)


def readFile():
    try:
        name = input("Enter file name to read : ")
        path = Path(name)

        if path.exists():
            with open(path,"r") as re:
                content = re.read()
                print(f"The File content is this :- \n {content}")
        else:
            print("File with this name not exist !!")
    except Exception as err:
        print("Error occur while reading file ",err)


def updateFile():
    name = input("Enter File Name : ")
    path = Path(name)

    if path.exists():
        
        print("Enter 1 for renaming the file name")
        print("Enter 2 for appending the file")
        print("Enter 3 for overriding the file")

        num = int(input("Enter your option :- "))

        if num == 1:
            try:
                newname = input("Enter File new name :- ")
                path2 = Path(newname)
                if not path2.exists():
                    path.rename(path2)
                    print("file name change successfully")
                else:
                    print("File already exist")
            except Exception as ex:
                print(f"Error while renaming {ex}")        


        elif num == 2:
            try:

                if path.exists():
                    with open(path,"a") as ap:
                        cont = input("Write a content to append in existing file :- ")
                        ap.write(cont)
                        print("Append successfully")
                else:
                    print("File not exist")
            except Exception as ex:
                print("Error while appending {ex}")

        elif num == 3:
            try:

                if path.exists():
                    with open(path,"w") as ap:
                        cont = input("Write a content to override in existing file :- ")
                        ap.write(cont)
                        print("Override successfully")
                else:
                    print("File not exist")
            except Exception as ex:
                print("Error while overriding {ex}")


    else:
        print("File name does not exist !!")    

def deleteFile():
    name = input("Enter file name to delete :- ")
    path = Path(name)

    try:
            
        if path.exists():
            path.unlink()
            print("File removed successfully")
        else:
            print("No such file exist")    
    except Exception as ex:
        print(f"Error occur while deleting file {ex}")
        







print("Please Enter 1 For Creating file")
print("Please Enter 2 For Reading file")
print("Please Enter 3 For Updating file")
print("Please Enter 4 For Deleting file")


userNum = int(input("Please Enter your number : "))


if userNum == 1:
    createFile()
if userNum == 2:
    readFile()
if userNum == 3:
    updateFile()
if userNum == 4:
    deleteFile()






