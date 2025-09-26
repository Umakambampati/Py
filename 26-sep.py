#first n natural numbers
def natural_numbers(n):
    if n<1:
        return
    natural_numbers(n-1)
    print(n)
natural_numbers(20)
            
#reverse natural numbers
def natural_numbers(n):
        if n<1:
            return
        print(n)
        natural_numbers(n-1)
n=10
natural_numbers(n)
#even numbers
def even_numbers(n):
    if n<0:
        return
    even_numbers(n-1)
    if n%2==0:
        print(n)
even_numbers(10)
        