t = int(input())
arr = [1,1,2,4]

for i in range(4, 68):
    arr.append(sum(arr[-4:]))

for i in range(t):
    n = int(input())
    print(arr[n])
