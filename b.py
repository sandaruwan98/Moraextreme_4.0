if __name__ == '__main__':
    p = int(input())
    q = int(input())
    r = int(input())
    phil= [0]*p
    smallest = [0]*p
    for i in range(p):
        phil[i] = int(input())

    for i in range(p):
        temparr=[0]*q
        for j in range(q):
            index=i+j
            if(index>=p):
                index-=p
            temparr[j]=phil[index]
        temparr.sort()
        smallest[i]=temparr[r-1]
    smallest.sort()
    print(smallest[0])