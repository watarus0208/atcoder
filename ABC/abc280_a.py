H, W = map(int, input().split())

cnt = 0
for h in range(H):
  S = input()
  for s in S:
    if s == '#':
      cnt += 1
print(cnt)