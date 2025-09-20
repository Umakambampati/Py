#print reverse and pallindrome
num=12421
temp=12421
rev=0
while num>0:
     rem=num%10
     rev=rev*10+rem
     num=num//10
print(rev)
print('pallindrome' if rev==temp else 'not a pallindrome')
#print even digit
num=12421
temp=12421
while num>0:
    rem=num%10
    if rem%2==0:
        print(rem)
    num=num//10
#print prime of digits
num=127578
prime=[2,5,7]
while num>0:
    rem=num%10
    if rem in prime:
        print(rem,end="")
    num=num//10
    
    #print perfect number
n=int(input("enter a number"))
sum=1
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        sum+=i
        if i!=n//i:
            sum+=n//i
if sum==n:
    print("perfect number")
else:
    print("not a perfect number")

    #in range
def perfect_number(start,end):
    for nums in range(start,end):
        sum= 1
        for i in range(2, int(nums**0.5) + 1):
            if nums % i == 0:
                sum+= i
                if i!=nums//i:
                  sum+=nums//i
        if sum== nums:
            print(nums, end=" ")
start=int(input("enter a number"))
end=int(input("enter a number"))
perfect_number(start,end)



