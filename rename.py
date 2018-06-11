import os
import shutil
from os import path

def main():
	# make a duplicate of an existing file
    if path.exists("loops.pycopied"):
        src=path.realpath("loops.pycopied")
        dst=src+"2"
        shutil.copy(src,dst)
        
    os.rename("loops.pycopied","loops1.py")
		
if __name__ == "__main__":
    main()