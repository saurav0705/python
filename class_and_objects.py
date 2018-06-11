class base():
    __name=""
    #constuctor
    def __init__(self,x):
        self.name=x
    def get(self,x):
        self.name=x
    def out(self):
        print(self.name)    
        

obj=base("shivam")
obj.out()
obj.get("saurav")
obj.out()
print(obj.name)