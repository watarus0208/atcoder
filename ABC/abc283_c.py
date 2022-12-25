s = input()
n = len(s)
i = 0 
cnt = 0
while i < n:
    if i != n-1:
        if s[i] == s[i+1] == '0':
            cnt += 1
            # print('s[i]:',s[i], 'cnt:',cnt)
            i += 2 
            # print('i:', i)
        else:
            cnt += 1
            # print('s[i]:',s[i], 'cnt:',cnt)
            i += 1
            # print('i:', i)
    else:
        cnt += 1 
        # print('s[i]:',s[i], 'cnt:',cnt)
        i += 1 
        # print('i:', i)

print(cnt)