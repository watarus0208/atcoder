import math
K = int(input())
S = math.ceil(math.sqrt(K))

for s in range(2,S):
    if K%s==0:
        if math.factorial(s)%K==0:
            print(s)
            break
else:
    print(K)

# ルジャンブルの定理
#  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
#   ○   ○   ○   ○    ○     ○     ○     ○     ○     ○ 
#       ○       ○          ○           ○           ○        