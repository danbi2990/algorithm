a,b,c = map(int,input().split())

def kang(a,b,c):
    if c-b == 1 and b-a == 1:
        return 0
    if c-b > b-a:
        return kang(b,c-1,c)+1
    else:
        return kang(a,a+1,b)+1

print(kang(a,b,c))
