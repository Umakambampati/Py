n=int(input("enter a number"))
temp=n
l=len(str(n))
sum=0
while temp>0:
    rem=temp%10
    sum+=rem**l
    temp=temp//10
if sum==n:
    print("armstrong")
else:
    print("not armstrong")

    
def arm_strong(start,end):
    for nums in range(start,end+1):
        temp=nums
        count=0
        while temp>0:
            count+=1
            temp=temp//10
        temp=nums
        sum=0
        while temp>0:
            rem=temp%10
            sum+=rem**count
            temp=temp//10
        if sum==nums:
            print(nums)
start=int(input("enter a number"))    
end=int(input("enter a number"))   
arm_strong(start,end)




        

