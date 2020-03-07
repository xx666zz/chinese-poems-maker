import sys,os,random,json
from pypinyin import pinyin
import thulac
thu1 = thulac.thulac()
qz={}
jy=input('几言：')
mjz=int(jy)*2+2
bzd=mjz/2
def fc(l):
    s=''
    qg={}
    for i in l:
        s+=i
    a=s
    text = thu1.cut(a, text=True)
    text=text.split(' ')
    for i in text:
        if i.endswith('_v'):
            w=i.split('_')[0]
            qg[w]=8
        if i.endswith('_n'):
            w=i.split('_')[0]
            qg[w]=8
        if i.endswith('_a'):
            w=i.split('_')[0]
            qg[w]=3
    return qg
def rd(name):
    lb=[]
    a=open(name,'r',encoding='utf-8')
    b=a.readlines()
    a.close()
    for i in b:
        o=i.replace(" ", "").strip("\n")
        if '，' in o and '。' in o and len(o)==mjz:
            lb.append(o)
    return lb
def sc(lb,j,p,l,zg,qj,qz):
    if j!=bzd and j!=mjz:
        if j==1:
            z1=[p]
        else:
            z=[]
            for i in lb:
                for i2 in range(zg):
                    if i2!=jy and i2!=mjz-1:
                        if i[i2] == l[i2]:
                            if i[j-1] in lll:
                                pass
                            else:
                                if j!=mjz-1 or pinyin(i[j-1], heteronym=1,style=5)==[[yun]]:
                                    for xx in range(zg+2-abs(i2-j)):
                                        #if xx>8:
                                            #break
                                        z.append(i[j-1])
                                    for iii in qz:
                                        if l[i2] in iii:
                                            for xx in range(qz[iii]):
                                                z.append(i[j-1])
            zd={}
            for i in z:
                if i in zd:
                    zd[i]=zd[i]+1
                else:
                    zd[i]=1
            z1=[]
            ii=-1
            for i1 in range(qj):
                max=0
                for i in zd:
                    if zd[i]>max:
                        max=zd[i]
                        ii=i
                if ii!=-1:
                    z1.append(ii)
                    zd[ii]=0
                else:
                    z1=sc(lb,2,'非',['非'],zg,qj,qz)
    elif j==mjz:
        z1=['。']
    elif j==bzd:
        z1=['，']
    return z1
lb=rd('a.txt')
l,jz={},{}
lll=[]
inp=input('头：')
yun=input('韵：')
for i in inp:
    j=0
    l[i]=[]
    while j<=mjz-1:
        j+=1
        x=random.sample(sc(random.sample(lb,99999),j,i,l[i],j-1,3,qz),1)
        l[i].append(x[0])
        lll.append(x[0])
        print(x[0],end='')
    jz[i]=''
    for i1 in l[i]:
        jz[i]+=i1
    print('')
print('')    
for qpq in range(10):
    for i in inp:
        for i1 in range(mjz):
            qz=fc(jz[i])
            x=random.sample(sc(random.sample(lb,99999),i1+1,i,l[i],11,1,qz),1)
            l[i][i1]=x[0]
            lll.append(x[0])
            print(x[0],end='')
        jz[i]=''
        for i3 in l[i]:
            jz[i]+=i3
        sj=jz[i]
        print('')
    print('')
