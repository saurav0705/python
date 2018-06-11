tup1=("robert","downy jr","50")
tup2=(1,2,3)
(name,cast,age)=tup1
tup3=(4,3,2)

def function():
    print("basics of tuple:")
    print(tup1[0])
    print(tup2[2])
    print(name)
    print(cast)
    print(age)
    if(tup2>tup3):
        print("tup1 is bigger")
    else:
        print("tup3 is bigger")    
    a = {'x':100, 'y':200}
    b = a.items()
    print(b)  

function()    