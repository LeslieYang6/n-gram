import test as a
import re
from decimal import *
context = Context(prec=100)
setcontext(context)
names=["[Shakespeare_William]_Complete_Works_Of_William_Sh(z-lib.org) (1).txt"]
P=a.getcount(names)
P1=0
p2=0
with open("test.txt",'r') as f:
    str=f.read()
    res=re.findall(r'(,|\.|\?|"|\w+)',str)
    p=Decimal(1.0)
    for i in range(0,len(res)-1):
        if res[i] in P and res[i+1] in P[res[i]]:
            p*=P[res[i]][res[i+1]]
        elif res[i] not in P:
            p*=Decimal(0.00000001)
        else:
            p*=P[res[i]]["SMOOTH!"]
    P1=p
    print(P1)

with open("test1.txt",'r') as f:
    str=f.read()
    res=re.findall(r'(,|\.|\?|"|\w+)',str)
    p=Decimal(1.0)
    for i in range(0,len(res)-1):
        if res[i] in P and res[i+1] in P[res[i]]:
            p*=P[res[i]][res[i+1]]
        elif res[i] not in P:
            p*=Decimal(0.00000001)
        else:
            p*=P[res[i]]["SMOOTH!"]
    P2=p
    print(P2)

print(P1>P2)