armstrong in range
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
start=int(input("enter 1st number"))    
end=int(input("enter last number"))   
arm_strong(start,end)

#check prime in range
def check_prime(start,end):
    for nums in range(start,end+1):
        is_prime=True
        if nums<2:
            is_prime=False
        for i in range(2,int(nums**0.5)+1):
            if nums%i==0:
                is_prime=False
                break
        if is_prime:
            print(nums)
start=int(input("enter starting number"))
end=int(input("enter ending number"))
check_prime(start,end)




        



