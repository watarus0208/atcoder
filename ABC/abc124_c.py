S = input()

b = 0
cnt = 0
for s in S:
    if b==0:
        b=1
    else:
        b=0
    if int(s) != b:
       cnt += 1 
print(min(cnt, len(S)-cnt))