list1=[10,20,30,-52,45]
list=[]
for i in range(len(list1)-1,-1,-1):
    list.append(list1[i])
print(list)


# inplace reverse approach(no extra memory)
list1=[10,20,30,-52,45]
lower=(len(list1)-1)//2
high=(len(list1)-1)
while lower<high:
    list1[lower],list1[high]=list1[high],list1[lower]
    lower+=1
    high-=1
print(list1)
#reverse of a string
str1="UmaMaheshwari"
str2=""
for char in str1:
    str2=char+str2
print(str2)
#method 2
str1="Raghu"
str1= str1[::-1]
print(str1)
#method 3
str1="uma"
str2=""
for i in range(len(str1)-1,-1,-1):
    str2+=str1[i]
print(str2)

#sum of digits if a number in list
def sum(list1):
    list2=[]
    for num in range(0,len(list1)):
        sum=0
        while list1[num]>0:
            rem=list1[num]%10
            sum+=rem
            list1[num]=list1[num]//10
        list2.append(sum)
    return list2
list1=[123,56,67,90]
print(sum(list1))

#maximum number of a digit
def max(num):
    digit=str(num)
    max=digit[0]
    while num>0:
        rem=num%10
        if rem>int(max):
            max=rem
        num=num//10
    return max
num=int(input("enter a number"))
print(max(num))

#maximum number of a digit in list
def max(list1):
    list2=[]
    for i in range(0,len(list1)):
        digit=str(i)
        max=digit[0]
        while list1[i]>0:
            rem=list1[i]%10
            if rem>int(max):
                max=rem
            list1[i]=list1[i]//10
        list2.append(max)
    return list2
list1=[20,33,456,789]
print(max(list1))
        






