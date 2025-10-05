#Check if a number is even or odd
num=int(input("enter a number:"))
if num%2==0:
    print("even")
else:
    print("odd")

#Find the maximum and minimum element in a list.
list1=[20,45,18,66,20]
max=list1[0]
min=list1[0]
for i in range(len(list1)):
    if list1[i]>max:
        max=list1[i]
    elif list1[i]<min:
        min=list1[i]
print(max)
print(min)

#Reverse a string without using slicing ([::-1] )
str1="umamaheshwari"
rev=""
for char in str1:
    rev=char+rev
print(rev)

#Check if a string is a palindrome.
str1=input("enter a string:")
str2=""
for char in str1:
    str2=char+str2
if str2==str1:
    print("palindrome")
else:
    print("not a palindrome")

#Find the factorial of a number (using loop)
num=int(input("enter a number"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)

#Count the frequency of each character in a string
str1="frequency"
dict1={}
for char in str1:
    if char in dict1:
        dict1[char]+=1
    else:
        dict1[char]=1
print(dict1)

#Find the second largest number in a list.
list1=[10,23,45,29,8]
largest=list1[0]
second_largest=list1[0]
for i in range(len(list1)):
    if list1[i]>largest:
        second_largest=largest
        largest=list1[i]
    elif list1[i]<largest and list1[i]>second_largest:
        second_largest=list1[i]
print(largest)
print(second_largest)

#Count how many vowels and consonants are in a string.
str1="QUestions"
str1=str1.lower()
vowels=0
consonants=0
for char in str1:
    if char in "aeiou":
          vowels+=1
    else:
        consonants+=1
print(vowels)
print(consonants)

#Calculate the sum of digits of a number.
num=int(input("enter a number"))
sum=0
while num>0:
    rem=num%10
    sum+=rem
    num=num//10
print(sum)

#Print the multiplication table of a number.
num=int(input("enter a number"))
for i in range(1,11):
    print(f"{num}x{i}={num*i}")

#Find the largest word in a given sentence.
str1="The longest word in a sentence"
str2=str1.split()
word="The"
longest=len(str2[0])
for i in range(1,len(str2)):
    if len(str2[i])>longest:
        longest=len(str2[i])
        word=str2[i]
print(word)

#Remove all duplicate elements from a list.
list1=[1,2,3,2,34,2,5,4,6]
unique=[]
for i in list1:
    if i not in unique:
        unique.append(i)
print(unique)

#Sort a list without using Python’s built-in .sort() 
list1=[4,3,1,0,5,6,9,22,2]
for j in range(0,len(list1)):
    for i in range(0,len(list1)-1-j):
        if list1[i]>list1[i+1]:
            list1[i],list1[i+1]=list1[i+1],list1[i]
print(list1)

#merge two lists into a single sorted list.
list1=[1,4,3,2]
list2=[3,2,1,0]
list1.extend(list2)
print(list1)
list1.sort()
print(set(list1))

#check if a number is a prime number.
num=int(input("enter a number"))
is_prime=True
if num<=1:
    is_prime=False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime=False
            break
if is_prime:
    print("prime")
else:
    print("not")
    









