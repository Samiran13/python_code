def defangIPaddr(address= str(input('enter your ipadress'))) -> str:
    
    xx = address.split('.')
    yy = ""
    for i in range(len(xx)):
        if i == len(xx) -1:
            yy = yy + xx[i]
        else:
            yy = yy + xx[i]
            yy = yy + '[.]'    

    print(yy)

defangIPaddr()        