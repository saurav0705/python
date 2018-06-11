import re
text_search='''123456789
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
sauravaggarwal98@gmail.com
sawantalwar@gmaail.com
uddcuidwbu@gmail.com
hwbcchiwbicwebic@gmail.com
154424215 street
holy shit
ha hah aha hahaha
new world'''



#regex and f gives the first word
def regex():
    n="coding is fun"
    n1=re.findall(r"^\w+",n)
    print(n1)
def f():
    xx = "guru99,education is fun"
    r1 = re.findall(r"^\w+",xx)
    print(r1)
def split():
    n='python is fun'
    print(re.split(r"\s",n))
def search():
    s=re.compile(r'h\W')
    match=s.finditer(text_search)
    for m in match:
        print(m)
    matchs=re.findall(r'[\w\.-]+@[\w\.-]+',text_search)
    for n in matchs:
        print(n)
    #\s means spaces and * after that means for any no. of words
    print (re.split(r'\s*',text_search))
    #if we include\s in () than it will show how they are seperated
    print(re.split(r'(\s*)',text_search))
    #if we remove \ it will consider s as a normal character
    print(re.split(r's',text_search))
    #we can also serach using ranges like for example [a-k]
    print(re.split(r'[a-k]',text_search))
    #we can also appy multiple ranges and also to make
    #it not case sensitive we can use flags like re.I==for ignoring case sensitivity
    #re.M==for multiline
    #to find a no. in a string we can use \d and for non number we can use \D
    

def fin():
    print (re.findall(r'\d',text_search))
    #{} brackets define the length i.e ex {1,9}
    print (re.findall(r'\w+\d{1,9}@\w+.\w+',text_search)) 
fin()
#search()
#split()
#regex()
