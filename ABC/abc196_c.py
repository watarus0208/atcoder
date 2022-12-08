N = int(input())

cnt = 1
while True:
    d = int(str(cnt)+str(cnt))
    if d <= N:
        cnt += 1
    else:
        print(cnt-1)
        break
