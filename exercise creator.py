import pandas as pd
import random

dataset = pd.read_csv("mido.csv", encoding='ISO-8859–1')

dataset=dataset.dropna(subset=['q'])

dataset=dataset.dropna()

pre=["of","Of","with","With","at","At","from","From","into","Into","during","During","including","Including","until","Until","against","Against","among","Among","despite","Despite","towards","Towards","upon","Upon","concerning","Concerning","to","To","in","In","for","For","on","On","by","By","about","About","through","Through","over","Over","before","Before","between","Between","after","After","since","Since","without","Without","under","Under","within","Within","along","Along","foloowing","Following","across","Across","behind","Behind","beyond","Beyond","but","But","except","Except","up","up","out","Out","around","Around","down","Down","off","Off","above","Above","near","Near"]

#punc=["much", "many", "some", "any", "few", "little", "each", "every","a few","a little"]
def convert(lst): 
    lst=lst.split() 
    for i in range (0, len(lst)):
        if lst[i] in pre:
            global answer
            answer=lst[i]
            if (answer[0]).isupper()==True:
                p=[lst[i],pre[i],pre[i+2]]
                random.shuffle(p)
                lst[i]=" ( "+p[0][0].upper()+p[0][1:]+" / "+p[1][0].upper()+p[1][1:]+" / "+p[2][0].upper()+p[2][1:]+" ) "
                break 
            else:
                p=[lst[i],pre[i],pre[i+2]]
                random.shuffle(p)
                lst[i]=" ( "+p[0][0].lower()+p[0][1:]+" / "+p[1][0].lower()+p[1][1:]+" / "+p[2][0].lower()+p[2][1:]+" ) "
                break
        
    return answer,lst
def convert2(a,lst):
    lst=lst.split()
    s=""
    for i in range (0,len(lst)):
        if a== lst[i]:
            lst[i]=len(lst[i])*"_"
    for i in range (len(lst)): 
        s+=lst[i]+" "
    return s,a

l=[]
ans=[]

for i in dataset['q']:
    a=convert(i)
    i,a=convert2(a,i)
    l.append(i)
    ans.append(a)
df=pd.DataFrame(ans)

lr=df[0].to_list()
lrr=df[1].to_list()

pi=[]
for i in lrr:
    s=""
    for k in i :
        s+=k+" "
    pi.append(s)

tr=pd.DataFrame(pi)

tr['answers']=lr

tr.to_csv('example2.csv',index=False)
