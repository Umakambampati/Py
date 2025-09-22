# def subset(arr1,arr2):
#     for i in arr1:
#         if i not in arr2:
#             return False
#     return True
# arr1=[1,2,3,4,6]
# arr2=[1,2,3,4,5,7,8]
# print(subset(arr1,arr2))
# a,b=0,1
# for i in range(10):
#     print(a)
#     a,b=b,a+b
a,b=0,1
for i in range(10,20):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        print("first prime is",i)
        while a<=i:
            print(a)
            a,b=b,a+b
        break

