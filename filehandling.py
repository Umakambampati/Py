###reading file
f=open('08.py','r')     #opening a file
print(f.read())            #reading the file as string
print(f.read(100))                  #read for 100 characters
print(f.readlines(100))           #readlines 
print(f.tell())             #at which position cursor is there
f.close()                 #close

with open('08.py','r') as f:
    for line in f:
        print(line,end="")        #difference between previous and this approach is previous definetly need toclose file current approach doesnot need to close implicity

# # writing  file
with open('10-sep.py','w') as f:
    f.write("changed version")

#appending file
with open('10-sep.py','a') as f:
    f.write("\n new line")

#copying file
with open('10-sep.py','r') as f:
    data=f.read()
with open('copy.py','w') as f:
    f.write(data)

# # file locations
import os
print(os.name)
print(os.getlogin())
print(os.getcwd())

with open(r"C:\Users\ADMIN\Desktop\problem solving\basic.py", "r", encoding="utf-8") as f:
    for line in f:
        print(line, end="")
