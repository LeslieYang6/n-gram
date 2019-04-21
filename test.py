import re
import random
import collections
import math
from decimal import *

def getcount(names):
    context = Context(prec=100)
    setcontext(context)
    dic={}
    for name in names:
         f=open(name,"r")
         str=f.read()
         res=re.findall(r'(\*|\+|>>|<<|\?|"|!|\.|,|\w+)',str)
         f.close()
         result=collections.Counter(res)
         dic={name:{} for name in result}
         length=len(res)
         for i in range(0,length-1):
             if res[i+1] in dic[res[i]]:
                 dic[res[i]][res[i+1]]+=1
             else:
                dic[res[i]][res[i+1]]=1
    p={name:{} for name in result}
    length=Decimal(len(dic))
    for a in dic:
        Sum=Decimal(sum([a for b,a in dic[a].items()]))+(length-len(dic[a]))*Decimal(0.01)
        for name in dic[a]:
            p[a][name]=Decimal(Decimal(dic[a][name])/Sum)
        SMOOTH=Decimal(Decimal(0.01)/Sum)
        p[a]["SMOOTH!"]=SMOOTH
    return p