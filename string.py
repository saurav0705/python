def strings():
    name="saurav"
    n="a"
    print("it gives value of character at that index:: "+name[1])
    print("it gives the value of strings upto which range is given (in this index 1-4)::: "+name[1:4])
    print("it gives a boolean expresion that is true or false base on that if that character exist in string(1st a in saurav and 2nd x in saurav) :::")
    print("a" in name)
    print("x" in name)
    print("not in method (example x not in saurav==true )")
    print("x" not in name)
    print("r'\n' prints \n and print R'/n' prints \n")
    number=5
    print("first name %s than number %d"%(name,number))
    number="999999"
    print("concatenating two strings "+(name+number))
    print("repeating strings::"+name*5)
    new_name=name.replace("av","xw")
    print("using replace function ::"+new_name)
    print(name.upper())
    print(name.capitalize())
    print(name.lower())
    print(":".join(name))
    print(";".join(reversed(name)))
    print(name.split("a"))
    new_name=name.replace("saurav","none")
    print(new_name)
strings()