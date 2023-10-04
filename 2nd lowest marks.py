N = int(input('How many students are there?? '))
final = dict()
for i in range(N):
    name = input('Name of the students-- ')
    marks = float(input('Entry the marks--'))
    final[name] = marks

#print(final)

num1 = list()
for k,v in final.items():
    num1.append(v)

#print(nums)
m = min(num1)
print(m)

num2 = list()
for i in range(len(num1)):
        if m != num1[i]:
            num2.append(num1[i])

#print(num2)
m1 = min(num2)
for key,value in final.items():
     if value == m1:
          print(f"The second lowest marks({value}) belongs to {key}")
                   

