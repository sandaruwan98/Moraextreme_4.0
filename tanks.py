if __name__ == '__main__':
    n = int(input())
    s = input()
    h = [int(x) for x in s.split()]
    vm=0
    for i in range(n):
        for j in range(i,n):
            x=[h[i],h[j]]
            m = min(x)
            dis = j-i
            
            v = m*dis
            if vm<v:
                vm = v
    print(vm)