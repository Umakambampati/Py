# Write a program to print middle character(s) in the given string or 
# number. 
string=input("enter a string")
length=len(string)
if length%2==0:
    middle=string[len(string)//2-1:len(string)//2+1]
    print(middle)
else:
    middle=string[len(string)//2]
    print(middle)
# Write a program to print the sum of the digits in the number. 
num=int(input("enter a number"))
sum=0
while num>0:
    rem=num%10
    sum+=rem
    num=num//10
print(sum)
#  Write a program to print reverse of the given number.  
num=int(input("enter a number"))
reverse=0
while num>0:
    rem=num%10
    reverse=reverse*10+rem
    num=num//10
print(reverse)
# • Write a program to print factorial of the number.
num=int(input("enter a number"))
fact=1
for i in range(1,num+1):
   fact=fact*i
print(fact)
# Write a program to check whether the sum of digits in the number except  
# first digit and digit is equal to the sum of first digit and last digit of that  number. If both the sums are equal then print equal otherwise print not  equal 

num1=(input("enter number"))
sum=int(num1[0])+int(num1[n-1])
num=int(num1[1:-1])
sum2=0
while num>0:
    rem=num%10
    sum2+=rem
    num=num//10
if sum==sum2:
    print("equal")
else:
    print("not equal")
#  Write a program to check whether the digits in-between the first and last  
# digit are less than first and last digit, if yes then print true, otherwise print  false. 
n=input("enter a string")
if n[1:len(n)]< n[0] and n[-1]:
    print("True")
else:
    print("False")
#  Write a program to print the vowels in the given string in reverse order.  
str1=input("enter a string")
rev=""
vowels="aeiouAEOU"
for char in str1:
    if char in vowels:
        rev=char+rev
print(rev)
# Write a program to print the vowels in the given string and repeated  vowel should be printed only single time.  
str1=input("enter a string")
vowels="aeiouAEIOU"
vowel=""
for char in str1:
   if char in vowels:
      if char not in vowel:
        vowel+=char
print(vowel)
#  Write a program to print the string after removing the duplicate characters  in the string.  
str1=input("enter a word")
freq={}
for char in str1:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
print(freq)
res=""
for char in str1:
   if freq[char]==1:
       res+=char
print(res)
# Write a program to convert all the upper case letters in the given string to  lower case letter and vice versa.  
s="Korean"
result=""
for char in s:
    if 'A'<=char<='Z':
        result+=chr(ord(char)+32)
    elif 'a'<=char<='z':
        result+=chr(ord(char)-32)
print(result)
# Write a program to print all the Upper case letters in the string in reverse  order and then followed by the lower case letters .  
str1=input("enter a string")
rev=""
lo=""
for char in str1:
    if 'A'<=char<='Z':
        rev=char+rev
    else:
        lo+=char
res=rev+lo       
print(res)
#  Find the Largest Element in an Array 
# Problem: Write a function to return the largest number in an array. 
def largest(list1):
    largest=list1[0]
    for i in range(len(list1)):
        if list1[i]>largest:
            largest=list1[i]
    return largest
list1=[3,1,4,1,5,9]
print(largest(list1))
# Find the Second Largest Element 
# Problem: Write a function to return the second largest number in an array. 
def second(list1):
    largest=list1[0]
    second=list1[0]
    for num in range(len(list1)):
        if list1[num]>largest:
            second=largest
            largest=list1[num]
        else:
            if list1[num]>second and list[num!=largest]:
                second=list1[num]
    return second
list1=[3,1,4,1,5,9]
print(second(list1))
# Sum of All Elements 
# Problem: Write a function that returns the sum of all elements in an array. 
def sum(list1) :
    sum=0
    for nums in list1:
        sum+=nums
    return sum
list1=[1,2,3,4]     
print(sum(list1)) 
#  Remove Duplicates from an Array 
# Problem: Write a function to remove duplicate values from an array.  
def duplicates(list1):
    dup=[]       
    for num in list1:
        if num not in dup:
            dup.append(num)
    return dup
list1=[1,2,2,3,4,4,5]
print(duplicates(list1))
#  Check if Array is Sorted 
# Problem: Write a function to check if an array is sorted in ascending  order. 
def sort(list1):
    for i in range(len(list1)-1):
        if list1[i]>list1[i+1]:
            return "False"
    return "true" 
list1=[1,8,3,4,5]
print(sort(list1))
# Reverse an Array 
# Problem: Write a function to reverse the elements in an array. 
def rev(arr):
    res=arr[::-1]
    return res
arr=[1,2,3,4,5]
print(rev(arr)) 
# Remove Falsy Values 
# Problem: Write a function that removes all falsy values from an array.  Falsy values include false, 0, "", null, undefined, and NaN. 
def falsy_values(list1):
    truthy=[]
    falsy=[]
    for num in list1:
        if num:
            truthy.append(num)
        else:
            falsy.append(num)
    return truthy,falsy
list1=[0,1,False,2,"",3]
print(falsy_values(list1))
# Find Unique Elements 
# Problem: Write a function to find the unique elements in an array  (elements that appear only once). 
def unique(list1):
    freq={}
    for num in list1:
        if num not in freq:
            freq[num]=1
        else:
            freq[num]+=1
    res=[]
    for num in list1:
        if freq[num]==1:
            res.append(num)
    return res
list1=[1,2,2,3,4,5]
print(unique(list1))
# ● Sum of Even Numbers 
# Problem: Write a function that returns the sum of all even numbers in an  array. 
def even(list1):
    sum=0
    for num in list1:
        if num%2==0:
            sum+=num
    return sum
list1=[1,2,3,4,5]
print(even(list1))
# Question: Write a function to reverse a given string.
str1=input("enter a string")
rev=""
for char in str1:
    rev=char+rev
print(rev)
# Check if a String is a Palindrome
str1=input("enter a string")
rev=""
for char in str1:
    rev=char+rev
print(rev)
if rev==str1:
    print("pallindrome")
else:
    print("not a pallindrome")
# Count Vowels in a String
# Question: Write a function to count the number of vowels in a given string.
str1=input("enter a string")
count=0
vowels="aeiouAEIOU"
remove=""
for char in str1:
    if char not in vowels:
        remove+=char
print(remove)
# Convert String to Title Case
# Question: Write a function that converts a string to title case (capitalize the first letter of each word).
str1=input("enter string")
result=str1.capitalize()
print(result)
# Convert String to Number
# Question: Write a function to convert a string to a number (without using parseInt or Number).
def string_integer(str1):
    res=0
    is_negative=False
    if str1[0]=='-':
        is_negative=True
        str1=str1[1:]
    for char in str1:
        if '0'<=char<='9':
            digit=ord(char)-ord('0')
            res=res*10+digit
    return -res if is_negative else res
# Check if String Contains Only Digits
# Question: Write a function to check if a string contains only numeric digits.
str1=input("enter string")
print(string_integer(str1))
str1=input("enter string")
is_number=True
for char in str1:
    if not ('0'<=char<='9'):
        is_number=False
print(is_number)
# Count Occurrences of a Character
# Question: Write a function that counts the occurrences of a specific character in a string.
str1=input("enter string")
target=input("enter char")
count=0
for char in str1:
    if char==target:
        count+=1
print(target,count)



        






















