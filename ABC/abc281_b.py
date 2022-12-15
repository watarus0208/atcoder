S = input()

if len(S)==8 and S[0].isupper() and S[1:7].isnumeric() and S[7].isupper():
    if 100000 <= int(S[1:7]) and int(S[1:7]) <= 999999:
        print('Yes')
    else:
        print('No')
else:
    print('No')
    

