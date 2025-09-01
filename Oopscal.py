class calculator:
    def addition(self,a,b):
        print(a+b)
    def subtraction(self,a,b):
        print(a-b)
    def multiplication(self,a,b):
        print(a*b)
    def division(self,a,b):
        if b!=0:
          print(a/b)
        else:
            print("Zero division error")
    def modulo_division(self,a,b):
        if b!=0:
          print(a%b)
        else:
            print("Zero division error")
    def floor_division(self,a,b):
        if b!=0:
          print(a//b)
        else:
            print("Zero division error")
    def exponential(self,a,b):
        print(a**b)
    def display(self):
        print("Model_number",self.Model_number)
        print("Made_In",self.Made_In)
        print("Color",self.Color)
        print("Discount",self.Discount)
cal1=calculator()
cal2=calculator()
print("\n Arthimetic operators with cal1")
cal1.addition(2,3)
cal1.subtraction(15,14)
cal1.multiplication(8,7)
cal1.division(12,5)
cal1.modulo_division(12,5)
cal1.floor_division(12,5)
cal1.exponential(2,4)
print("\n adding model_number,made_in to obj1(cal1)")
cal1.Model_number="Casio fx-991EX"
cal1.Made_In="Japan"
cal1.Color="Not Assigned"
cal1.Discount="Not Assigned"
cal1.display()
print("\nAfter updation")
cal1.Model_number="Casio fx-991EX"
cal1.Made_In="Japan"
cal1.Color="Silver"
cal1.Discount="30%"
cal1.display()
print("\n Arthimetic opretors with cal2")
cal2.addition(5,8)
cal2.subtraction(100,60)
cal2.multiplication(78,3)
cal2.division(133,0)
cal2.modulo_division(14,7)
cal2.floor_division(67,5)
cal2.exponential(5,7)
print("\n adding color,discount to obj2(cal2)")
cal2.Model_number="Not Assigned"
cal2.Made_In="Not Assigned"
cal2.Color="grey"
cal2.Discount="20%"
cal2.display()
print("\n after updation")
cal2.Model_number="Texas Instruments TI-84 Plus"
cal2.Made_In="USA"
cal2.Color="grey"
cal2.Discount="20%"
cal2.display()

