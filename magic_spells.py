import itertools
n = int(input())
b = ['1']*n
res=[]

def swapAll(s,rp,yp):
    
    for i in range(len(b)):
     if b[i]=='1':
        b[i] ='0'
     else:
        b[i]='1'
    recur(s-1,rp,yp)

def swapOdd(s,rp,yp):
    global b
    for i in range(len(b)):
        if i%2==1:
            if b[i]=='1':
                b[i] ='0'
            else:
                b[i]='1'
    recur(s-1,rp,yp)


def swapEven(s,rp,yp):
    global b
    for i in range(len(b)):
        if i%2==0:
            if b[i]=='1':
                b[i] ='0'
            else:
                b[i]='1'
    recur(s-1,rp,yp)


def toggle(s,rp,yp):
    global b
    for i in range(len(b)):
        if i%3=='1':
            if b[i]=='1':
                b[i] ='0'
            else:
                b[i]='1'
    recur(s-1,rp,yp)
    
def check(rp,yp):
    flag = True
    for r in rp:
        if r!='-1':
            
            ir=int(r)
            if(b[ir-1] != '1'):
                flag = False
                return flag
    for y in yp:
        if y!='-1':
            iy=int(y)
            if(b[iy-1] != '0'):
                flag = False
                return flag
    
    return flag

def recur(s,rp,yp):
    global b
    if s<=0:
        if(check(rp,yp)):
            res.append(''.join(b))
        
        b=['1']*n
       
        return
    swapAll(s,rp,yp)
    swapEven(s,rp,yp)
    swapOdd(s,rp,yp)
    toggle(s,rp,yp)
    
    


s = int(input())
rp = input()
yp = input()
rp = rp.split(" ")
yp = yp.split(" ")

recur(s,rp,yp)
res = sorted(set(res), key=res.index)
# print(res)
for target_list in res:
    print(target_list)
