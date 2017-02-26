
# 2941
# s = input()
# a = ["c=","c-","dz=","d-","lj","nj","s=","z="]
# r = 0
# for i in range(len(a)):
#     r += s.count(a[i])
#     s = s.replace(a[i],"")
# r += len(s)
# print(r)
# import re;print(len(re.findall('dz=|[csz]=|[dc]-|[ln]j|.',input())))


# 5622
# print(sum((ord(c)-65-(c=='Z')-(c>='S'))//3+3for c in input()))
# print(sum((ord(c)-64)*28//89+3-(c>'Y')for c in input()))


# 2908
# a,b = input().split()
# print(max(int("".join(reversed(a))), int("".join(reversed(b)))))
# a = [1,2,3]
# s = "123"
# print(int(s[::-1]))


# 1316: fail
# t = int(input())
# res = 0
# for i in range(0,t):
#     a = [0] * (ord('z') + 1)
#     s = input()
#     if len(s) < 3:
#         res += 1
#     else:
#         flag = True
#         a[ord(s[0])] = 1
#         for j in range(1,len(s)):
#             if s[j] != s[j-1]:
#                 a[ord(s[j])] += 1
#             if a[ord(s[j])] > 1:
#                 flag = False
#                 break
#         if flag:
#             res += 1
# print(res)


# 1157
# s = input().upper()
# l = list(map(s.count, [c for c in map(chr,range(65,91))]))
# m = max(l)
#
# if l.count(m) > 1:
#     print("?")
# else:
#     print(chr(l.index(m)+65))

