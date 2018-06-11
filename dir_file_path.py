import os.path
from os import path
def f():
    print (path.exists("loops.py"))
    print (path.isfile("loops.py"))
    print (path.isdir("__pycache__"))
    print (os.name)


f()