# Find the missing numbers. Input: 34571  	Output : 26 missing
num1=34571
list1=[]
while num1>0:
    rem=num1%10
    list1.append(rem)
    num1=num1//10
print(list1)
list1_min=min(list1)
list1_max=max(list1)
for i in range(list1_min,list1_max):
    if i not in list1:
        print(i)

# "Given a list where each element represents the color of a sock, e.g., ['red', 'green', 'red', 'purple', 'green', 'black', 'red'], how many days can I sustain if I can wear only one matching pair of socks per day and each pair can be used only once?"

# list1=['red','green','red','purple','green','black','red','purple']
dict1={}
for i in list1:
    if i not in dict1:
        dict1[i]=1
    else:
        dict1[i]+=1
print(dict1)
count=0
for key,value in dict1.items():
    if value>=2:
        count+=1
print("No of days you can wear",count)

# Matrix addition using range.
list1=[[1,2,3],[3,4,5],[7,9,0]]
total_sum=0
for i in range(len(list1)):
    for j in range(len(list1[0])):
        total_sum+=list1[i][j]
print(total_sum)