#allzeros
l=[[11,22,33],[44,55,66],[77,88,99]]
for i in range(len(l)):
    for j in range(len(l)):
        l[i][j]=l[i][j]-l[i][j]
print(l)

# sum of rows
l=[[11,22,33],[44,55,66],[77,88,99]]
l2=[]
for i in range(len(l)):
    sum=0
    for j in range(len(l)):
        sum+=l[i][j]
    l2.append(sum)
print(l2)

#rightzero
l=[[11,22,33],[44,55,66],[77,88,99]]
j_index=len(l)-1
for i in range(len(l)):
    for j in range(len(l)):
        if j==j_index:
            print(0,end=" ")
            j_index-=1
        else:
            print(l[i][j],end=" ")
    print()
#left zero
l=[[11,22,33],[44,55,66],[77,88,99]]
for i in range(len(l)):
    for j in range(len(l)):
        if i==j:
            l[i][j]=0
print(l)

