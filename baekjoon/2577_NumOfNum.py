A = int(input())
B = int(input())
C = int(input())
D = A * B * C
E = [0] * 10

while D != 0:
    F = D % 10
    D //= 10
    E[F] += 1
for i in range(10):
    print(E[i])
