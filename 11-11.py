try:
    num1=int(input("enter a number"))
    num2=int(input("entera number"))
    print(num1/num2)
except ZeroDivisionError:
    print("zero division error")

finally:
 print("code exceuted")
try:
    num1=int(input("enter a number"))
    num2=int(input("enter a number"))
    print(num1/num2)
except Exception as e:
    print(e)
else: 
    print("correct code") 
# ###############################      
# try:
#     num1=int(input("enter a number"))
#     num2=int(input("enter a number"))
# else:
#    print("code is executed")        #expected 'except or finally block"
############################################3
try:
    num1=int(input("enter a number"))
    num2=int(input("enter a number"))
    print(num1/num2)
finally:
    print("code completed")      #prints results and executes finally block if exception occurs after finally block exception raises
###---------------nested try---------------------------
try:
    num1=int(input("enter a number"))
    num2=int(input("enter a number"))
    print(num1/num2)
    try:
        num3=int(input("enter a number"))
        num4=int(input("enter a number"))
        print(num3/num4)
    except ZeroDivisionError:
        print("should not be divided with zero")
except Exception as e:
    print("enter correct data type")



