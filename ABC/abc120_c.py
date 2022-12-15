S = input()

ans = min(S.count('1'), S.count('0'))*2
print(ans)

#t = []
#for c in S:
#    if t and t[-1] != c:
#        t.pop()
#    else:
#        t.append(c)
#ans = len(S) - len(t)
