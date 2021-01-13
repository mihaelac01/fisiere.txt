with open('globulete.txt','r') as f:
    a=f.readline()
b=int(a)+3
d=int(a)+b-2
s=int(a)+b+d
with open('bradut.txt','w') as f:
    f.write(str(s))