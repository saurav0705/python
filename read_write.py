import re
def f_write():
    f=open("read&write.txt","w+")
    for i in range (1,20):
        f.write("This is %d line\n"%i)
    j=open("read&write.txt","a+")
    j.write("This is the appended text")
    f.close()
def f_read():
    f=open("read&write.txt","r")
    if f.mode=="r":
        contents=f.read()
        print(re.findall(r"This\sis\s\d\w+",contents))
    else:
        print("none")



#f_write()
f_read()