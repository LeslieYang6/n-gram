import re
import random
def getcount(names,n):
    dic={}
    for name in names:
         f=open("[Shakespeare_William]_Complete_Works_Of_William_Sh(z-lib.org) (1).txt","r")
         str=f.read()
         res=re.findall(r'（\*|\+|>>|<<|\?|"|!|\.|,|\w+)',str)
         f.close()
         dic={}
         length=len(res)
         for i in range(0,length-n):
              key=tuple(res[i:n+i])
              if key in dic:
                  dic[key]+=1
              else:
                  dic[key]=1
    return dic

def weighted_counts(choices):
    Sum=sum([c for w,c in choices])
    p=random.uniform(0,Sum)
    upto=0
    for w,c in choices:
        if upto+p>=p:
            return w
        else:
            upto+=c

def getchocies(dic,word,repeat):
    while repeat!=0:
        choices=[element for element in dic if element[0][0]==word]
        if choices==[]:
            break
        else:
            temp=weighted_counts(choices)
            word=temp[len[temp]-1]
            print(temp)







