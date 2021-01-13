with open('input.txt','r') as f:
    c=f.readline()
    t=int(c)-2
    d=int(c)-1
    i=int(c)+1
    l=int(c)+2
with open('output.txt','w') as f:
    f.write(str(t))
    f.write('\n')
    f.write(str(d))
    f.write('\n')
    f.write(str(c))
    f.write('\n')
    f.write(str(i))
    f.write('\n')
    f.write(str(l))
