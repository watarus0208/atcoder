N, X, Y = map(int, input().split())

red = [0]*N
blue = [0]*N
red[N-1] = 1

while N>1:
    red[N-2] += (X+1)*red[N-1]
    blue[N-2] += X*Y*red[N-1]
    red[N-2] += blue[N-1]
    blue[N-2] += Y*blue[N-1]
    red[N-1] = 0
    blue[N-1] = 0
    N -= 1

print(blue[0])

    
# red_n = red_n-1 + X*(red_n-1 + Y*blue_n-1)
#       = (X+1)*red_n-1 + XY*rblue_n-1
# blue_n = red_n-1 + Y*blue_n-1