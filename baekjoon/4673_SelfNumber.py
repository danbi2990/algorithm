
def gen(i):
    return i + gen2(i)


def gen2(i):
    if i < 10:
        return i
    return i % 10 + gen2(i / 10)

li = [gen(x) for x in range(1, 10001)]

res = [x for x in range(1, 10001) if x not in li]
for j in range(0, len(res)):
    print(res[j])
