# with open("new.txt","w") as file:
#     file.write("This is the new line")
#     file.close()


# with open("new.txt","a") as f:
#     f.write("\n This is the new line i have added")
#     print("apped completed")
#     f.close()


# f = open("new.txt","r")
# print(f.read())

# with open("op.txt","x") as f:
#     f.write("Execute new file")
#     print("Completed")


# try:
#     with open("op.txt","x") as ne:
#         ne.write("check existence")
#         print("Not exists")
# except Exception as e:
#     print("File already exist",e)




with open("sample.txt","r") as f:
    con = f.read()

con = con.replace("Java","python")

with open("sample.txt","w") as n:
    n.write(con)
















