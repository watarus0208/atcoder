n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(len(a)):
    for j in range(i):
        if (a[i] - a[j])%200==0:
            ans += 1

print(ans)