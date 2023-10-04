def decodeMessage(key=str(input('KEY: ')), message=str(input('MSG: '))) -> str:
    string =""
    for char in key.replace(" ",""):
        if char not in string:
            string=string+char

    list1 = []
    list1.extend(string)
    list2 = []
    list2.extend('abcdefghijklmnopqrstuvwxyz')
    list = {}
    for i in range(26):
        list[list1[i]] = list2[i]
    print(list)
    s = ""
    for ch in message:
        if ch == " ":
            s = s + " "
        else:
            s = s + list[ch]

    print(s)    



decodeMessage()
