def dictionary():
    name={'saurav':99,'sawan':66,'shivam':55}
    print(name['sawan'])
    x=name.copy()
    print(x)
    x.update({'sawan':'chutiya'})
    print(x)
    del x['sawan']
    print(x)
    print("this is the list %s"% name.items())
    sub_name={'sawan':55}
    sub_name2={'ranjan':77}
    for key in sub_name.keys():
        if key in name.keys():
            print("true")
        else:
            print("false")    
    Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
    print("printable string:%s" % str (Dict))        


dictionary()    