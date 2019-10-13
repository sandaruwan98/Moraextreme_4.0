
def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 

x = input()
x=x.split(',')
x=[int(i) for i in x]
a=x

ar1,ar2,ar3 = [],[],[]

x=1/a[0]
for i in range(a[0]):
    ar1.append(x*i)
x=1/a[1]
for i in range(a[1]):
    ar2.append(x*i)
x=1/a[2]
for i in range(a[2]):
    ar3.append(x*i)
list1= intersection(ar1,ar2)
list1= intersection(list1,ar3)
# print(list1) 

def isIN(l, r): 
   
    global list1
    for x in list1: 
        if x> l and x< r:     # print("f")
            return True
        elif(l==x and r==x):
            return True
    return False 

    
for i in range(a[3]):
    qs=input()
    qs=[int(j) for j in qs.split(',')]
    x=1/a[qs[0]-1]
    r1=[x*(qs[1]-1),x*(qs[1])]
    x=1/a[qs[2]-1]
    r2=[x*(qs[3]-1),x*(qs[3])]
    # if (r1[0]<=r2[0]):
       
    #     s=[r1[1],r2[0]]
    # else:
    #     s=[r1[0],r2[1]]
    s=[r1[1],r2[0]]
    s.sort()
    s1=[r1[0],r2[1]]
    s1.sort()
    if (isIN(s[0],s[1])):
        # print(s)
        print("NO")
    elif (isIN(s1[0],s1[1])):
        # print(s1)
        print("NO")
    else:
        print("YES")
