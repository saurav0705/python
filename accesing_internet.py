import urllib.request
def check_connection():
    flag=urllib.request.urlopen("https://www.youtube.com/")
    
    if(flag.getcode()==200):
        print ("connection established")
    else:
        print ('connection unsuccessful')

check_connection()