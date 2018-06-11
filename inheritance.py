class base():
    number=""
    def get(self,x):
        self.number=x
    def attr(self):
        print(self.number)

class child(base):
    num2=""
    def __init__(self,x):
        self.num2=x
        base.get(self,x)
    def out(self):
        print(self.num2)

c=child(25)
c.out()
c.attr()
print(isinstance(child,base))