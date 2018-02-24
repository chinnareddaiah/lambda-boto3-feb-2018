class Calculator:
    def add(self,x,y):
        return x+y

    def mul(self,x,y):
        return x*y

# Creating object for a Calculator
cal = Calculator()
x = cal.add(10,20)
y = cal.mul(10,15)
print('{} and {}'.format(x,y))
