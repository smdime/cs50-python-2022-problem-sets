exp = input("Expression: ")
x, y, z = exp.split(" ")
if y == "+":
    print(round(float(x)+float(z),1))
elif y =="-":
    print(round(float(x)-float(z),1))
elif y =="*":
    print(round(float(x)*float(z),1))
else:
    print(round(float(x)/float(z),1))