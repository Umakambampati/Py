str1="aabcca"
result=""
prev=str1[0]
count=1
for i in range(1,len(str1)):
    if str1[i]==str1[i-1]:
        count+=1
    else:
        result+=prev+str(count)
        count=1
        prev=str1[i]
result+=prev+str(count)
print(result)

list1=[100,56,-34,78,67]
for j in range(0,len(list1)):
    for i in range(0,len(list1)-1-j):
        if list1[i]<list1[i+1]:
            list1[i],list1[i+1]=list1[i+1],list1[i]
print(list1)

str1="cvbhjk"
list1=list(str1)
for j in range(0,len(list1)):
    for i in range(0,len(list1)-1-j):
        if list1[i]>list1[i+1]:
            list1[i],list1[i+1]=list1[i+1],list1[i]
res=""
for i in list1:
    res+=i
print(res)

list1=["abc","defg","hijklmn","ty","i"]
for j in range(0,len(list1)):
    for i in range(0,len(list1)-1-j):
        if len(list1[i])>len(list1[i+1]):
            list1[i],list1[i+1]=list1[i+1],list1[i]
print(list1)

list1=[[2,1],[8,7,3],[0,9,5],[7,2],[1,8,1]]
for innerlist in list1:
    for j in range(0,len(innerlist)):
        for i in range(0,len(innerlist)-1-j):
            if innerlist[i]>innerlist[i+1]:
                innerlist[i],innerlist[i+1]=innerlist[i+1],innerlist[i]
print(list1)
for k in range(0,len(list1)):
    for m in range(0,len(list1)-1-k):
        if list1[m][0]>list1[m+1][0]:
            list1[m],list1[m+1]=list1[m+1],list1[m]
print(list1)
