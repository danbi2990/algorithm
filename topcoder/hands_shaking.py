
n = int(input())
d = [0]*(n+1)
d[2] = 1

for i in range(4,n+1,2):
	for k in range(1,i,2):
		d[i] += d[k-1]*d[i-k-1]

print(d[n])
