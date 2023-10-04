roman = str(input())
x = list()
x.extend(roman.upper())
print(x)
values = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
total =0
for i in range(len(x) -1):
    if values[x[i]] < values[x[i+1]]:
        total = total - values[x[i]]
    else:
        total = total+values[x[i]]

num = total + values[x[-1]]
print(num)        

     
    