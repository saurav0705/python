def loops():
    x=0
    while(x<4):
        print(x)
        x+=1
    n=11
    for x in range(4,n):
        print(x)
        x+=1
    name=('a','b','c','d')
    for i,n in enumerate(name):
        if(n!='b'):
            print(i,n)
        else:
            continue  
    for i in '123456789':
        print("name")      

loops()    