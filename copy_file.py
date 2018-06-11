from datetime import date ,time,timedelta
import time
import datetime
from os import path
import shutil
def f():
    if(path.exists("loops.py")):
        info=path.realpath("loops.py")
        location,name=path.split(info)
        print ("location:: "+location)
        print ("name:: "+name)
        dst=info+"copied"
        #copy only copies metadata but if we use copystat it will create it with meta data and permission and other info
        shutil.copy(info,dst)
         # Get the modification time
        t = time.ctime(path.getmtime("loops.py"))
        print(t)
        print(datetime.datetime.fromtimestamp(path.getmtime("loops.py")))
    else:
        print("none file exist")

f()