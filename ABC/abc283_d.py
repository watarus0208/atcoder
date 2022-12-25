S = input()

c = set()
stk = []

for s in S:
    if s=='(':
        stk.append('(')
    elif s!='(' and s!=')':
        stk.append(s)
        if s in c:
            print('No')
            exit()
        else:
            c.add(s)
    elif s==')':
        while True:
            t = stk.pop()
            if t == '(':
                break
            elif t != '(':
                c.remove(t)        

print('Yes')            