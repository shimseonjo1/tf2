class Calculator:
    sum = 100
    def __init__(self):
        self.result = 0
    
    def add(self,num):
        self.result += num
        return self.result


cal1 = Calculator()
cal2 = Calculator()
# cal1.result=2
# cal2.result=9

# print(cal1.result)
# print(cal2.result)
# print(Calculator.sum)
# Calculator.sum=2001
# print(cal1.sum)
# print(cal2.sum)

cal1.add(3)
cal1.add(4)
print(cal1.result)
print(cal2.result)

class FourCal(Calculator):
    def sub(self,num):
       self.result -= num
       return self.result 

cal3 = FourCal()
cal4 = FourCal()

cal3.add(5)
cal3.sub(3)
print(cal3.result)