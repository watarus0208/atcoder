n, k = map(int, input().split())
a = list(map(int, input().split()))
#print(n, k)
#print(a)
cnt = 0
for i in range(n):
    sum = 0
    j = i
    while j < n:
        sum += a[j]
        if sum <= k:
            #print('sum:',sum)
            #print('j:', j)
            cnt += 1
            j += 1
        else:
            break

print(cnt)