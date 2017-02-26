# 10250
# exec('a,b=map(d,c().split(" "));print(d((4*(b-a)-3)**0.5));'*x)
exec('a,b,c=map(int,input().split(" "));print(str(c%a if c%a!=0 else a)+str(c//a+1 if c%a!=0 else c//a).zfill(2));'*int(input()))


# 1011

# def dfs(k, r):
#     if r == 1:
#         return 1
#     if (k+1)*(k+2)//2 <= r:
#         return dfs(k+1,r-(k+1)) + 1
#     elif k*(k+1)//2 <= r:
#         return dfs(k, r - k) + 1
#     else:
#         return dfs(k-1, r - (k-1)) + 1

# t=int(input())
# while(t!=0):
#     a,b=map(int,input().split())
#     d = b-a-1
#     k = 1
#     r = 1
#     while(d!=0):
#         if (k+1)*(k+2)//2<=d:
#             k = k+1
#         elif k*(k+1)//2<=d:
#             pass
#         else:
#             k = k - 1
#         d-=k
#         r+=1
#     print(r)
#     t-=1


# 1193
# n = int(input())
# i = 1
# while (i*i-i+2)/2 < n:
#     k = (i*i-i+2)//2
#     i += 1
# print(i,k)
# print(n-k+1,'/',i-n-k)

# 2292
# n = int(input())
# i = 1
# while 3*i**2-3*i+1 < n:
#     i += 1
# print(i)
