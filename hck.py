import re
def function():
    x=str(input())
    a=x.split(" ")
    val_x=int(a[0])
    t_val=int(a[1])
    #print (b,d)
    c=str(input())
    s=c.split(" ")
    sum=0
    counter=0
    previous=None
    print (s)
    for i in s:
        
        if(re.findall(r"x",i)):
            n=re.findall(r"\d",i)
            m=re.findall(r"\*\*\d",i)
            #print(m)
            #print (n)
            if(m):
                if(counter==0):
                    sum=sum+val_x**int(n[0])
                else:
                    if(previous=='+'):
                        if(len(n)==2):
                            sum=sum+int(n[0])*(val_x**int(n[1]))
                        else:
                            sum=sum+val_x**int(n[0])
                        
                    else:
                        if(len(n)==2):
                            sum=sum-int(n[0])*(val_x**int(n[1]))
                        else:
                            sum=sum-val_x**int(n[0])
                        
            else:
                if(previous=='+'):
                    if(len(n)==1):
                        sum=sum+int(n[0])*val_x
                    else:
                        sum=sum+val_x
                    
                else:
                    if(len(n)==1):
                        sum=sum-int(n[0])*val_x
                    else:
                        sum=sum-val_x
                    
                
        else:
            #print (i)
            k=re.findall(r"\d",i)
            #print (k)
            #sum=sum+int(k[0])
            if(len(k)!=0):
                if(previous=='+'):
                    sum=sum+int(i);
                else:
                    sum=sum-int(i);
        previous=i      
            
    #print (sum)
    if(t_val==sum):
        print ("True")
    else:
        print ("False")


if __name__=="__main__":
    function()