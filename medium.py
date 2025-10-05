#Find all pairs in a list that sum up to a target value.
list1=[20,55,23,64,71]
target=10
list2=[]
for i in range(len(list1)):
    sum=0
    temp=list1[i]
    while temp>0:
        rem=temp%10
        sum+=rem
        temp=temp//10
    if sum==target:
        list2.append(list1[i])
print(list2)

#Implement a program to rotate a list by k positions.
list1=[1,2,3,4,5,6,7]
k=2
for i in range(k):   #right rotation
    last=list1.pop()
    list1.insert(0,last)
print(list1)

list1=[1,2,3,4,5,6,7]
k=2
for i in range(k): #left rotation
    first=list1.pop(0)
    list1.append(first)
print(list1)

#Find the missing number in a list of consecutive integers.
list1=[2,3,4,6,7]
missing=0
for i in range(min(list1),max(list1)):
    if i not in list1:
        missing=i
print(missing)

#Check if two strings are anagrams.
str1="listen"
str2="silent"
str1=list(str1)
str2=list(str2)
str1.sort()
str2.sort()
if str1==str2:
    print("anagram")
else:
    print("not anagram")

#Count the number of words in a sentence
str1="Number of words in a sentence"
str2=str1.split()
count=0
for i in str2:
    count+=1
print(count)
    
#Remove all duplicate words from a sentence.
str1="Duplicate words in a sentence a words"
str1=str1.split()
str2=[]
for i in str1:
    if i not in str2:
        str2.append(i)
str3=' '.join(str2)
print(str3)

#Given a dictionary, invert it (keys become values).
dict1={'arun':1,'bunny':2,'chintu':3}
dict2={}
for key,value in dict1.items():
    dict2[value]=key
print(dict2)

#Find the intersection of two lists.
list1=[1,2,3]
list2=[2,3,4]
list3=[]
for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i]==list2[j]:
            list3.append(list1[i])
print(list3)

#Print the transpose of a matrix.
matrix1=[[1,2,3],
       [4,5,6],
       [7,8,9]]
n=len(matrix1)
for i in range(n):
    for j in range(i+1,n):
        matrix1[i][j],matrix1[j][i]=matrix1[j][i],matrix1[i][j]
print(matrix1)

#Implement bubble sort.
list1=[3,2,4,5,1,8,6]
for i in range(len(list1)):
    for j in range(len(list1)-1-i):
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
print(list1)

#Find the first non-repeating character in a string
str1="nonrepeating"
dict1={}
for char in str1:
    if char not in dict1:
        dict1[char]=1
    else:
        dict1[char]+=1
for key,value in dict1.items():
    if value==1:
        print(key)
        break

#Find the longest word in a sentence.
str1="The longest word in a sentence"
str2=str1.split()
word="The"
longest=len(str2[0])
for i in range(1,len(str2)):
    if len(str2[i])>longest:
        longest=len(str2[i])
        word=str2[i]
print(word)

#Find the second smallest number in a list.
list1=[2,1,3,4,5,6]
smallest=list1[0]
second=list1[0]
for i in range(1,len(list1)):
    if list1[i]<smallest:
        second==smallest
        smallest=list1[i]
    else:
        if list1[i]<smallest and list1[i]>second:
            second=list1[i]
print(second)

#Implement a program to check if a number is an Armstrong number.
num=int(input("enter a number"))
sum=0
temp=num
n=len(str(num))
while temp>0:
    rem=temp%10
    sum+=rem**n
    temp=temp//10
if sum==num:
    print("armstrong")
else:
    print("not armstrong")
