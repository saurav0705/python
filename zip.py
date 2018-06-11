import os
import shutil
from zipfile import ZipFile
from os import path
from shutil import make_archive

def f():

    # Check if file exists
    if path.exists("read&write.txt"):

    # get the path to the file in the current directory
        src = path.realpath("read&write.txt")
    # rename the original file
        os.rename("read&write.txt","read&write2.txt")
    # now put things into a ZIP archive
        root_dir,tail = path.split(src)
        shutil.make_archive("archive","zip",root_dir)
        print ("success")
    # more fine-grained control over ZIP files
    with ZipFile("python.zip", "w") as newzip:
        newzip.write("read&write2.txt")
        newzip.write("loops.pycopied2")
f()    