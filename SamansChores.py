import collections
lst = collections.deque()

def index(element, queue):
     for i, ele in enumerate(queue):
         if ele == element:
             return i
     return -1

if __name__ == '__main__':
    z = input()
    z=z.split()
    l= int(z[1])
    for i in range(l):
        x = input()
        x=x.split()
        n1,n2=index(x[0],lst),index(x[1],lst)
        


        if (n1 == -1 and n2 ==-1):
            lst.append(x[0])
            lst.append(x[1])
        elif(n1 == -1 and n2 !=-1):
            if n2>0:
                lst.insert(n2,x[0])
            else:
                lst.appendleft(x[0])
        elif(n1 != -1 and n2 ==-1):
            lst.insert(n1+1,x[1])
        elif(n1 != -1 and n2 !=-1):
            pass
    z = input()
    z=z.split()
    print(lst)