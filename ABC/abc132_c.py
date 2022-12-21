N = int(input())
d = sorted(list(map(int, input().split())))

while len(d)>2:
    d.pop(0)
    d.pop(-1)

print(d[1]-d[0])