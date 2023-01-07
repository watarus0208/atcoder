N = int(input())
P = list(map(int, input().split()))

for i in range(N-1):
    #print(-i-1, -i-2)
    #print(P[-i-2], P[-i-1])
    if P[-i-2] > P[-i-1]:
        #P[i-2]の値を今のP[i-2]の次に小さい値に設定する
        ans = P[:-i-2]
        #print('ans:',ans)
        tail = sorted(P[-i-2:], reverse=True)
        #print('tail:', tail)
        j = tail.index(P[-i-2])+1
        #print('j', j)
        ans.append(tail.pop(j))
        ans.extend(sorted(tail, reverse=True))
        print(*ans)
        exit()

        
        
