def rangegen(limit):
    num1=0
    while num1<limit:
        temp=num1
        num1+=1
        yield temp
       
values=rangegen(10)
print(next(values))
print("hey hii")
print(next(values))
print("its second iteration")
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))


def fibonaccigen():
    num1=0
    num2=1
    while True:
        yield num1
        num1,num2=num2,num1+num2
fib=fibonaccigen()
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))


    
