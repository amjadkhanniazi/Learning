class Calculator:
    def __init__(self,a=0,b=0):
        self.a=a
        self.b=b
    def sum(self):
        return self.a+self.b
    def mult(self):
        return self.a*self.b
    def sub(self):
        return self.a-self.b
    def div(self):
        if self.b!=0:
            return self.a/self.b
        else:
            return "Error: Division by Zero"


calc=Calculator(10,5)
print(f"Numbers: {calc.a}, {calc.b}")
print(f"Sum: {calc.sum()}")
print(f"Multiplication is: {calc.mult()}")
print(f"subtraction: {calc.sub()}")
print(f"Division: {calc.div()}")
