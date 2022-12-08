import math

A, B, H, M = map(int, input().split())

h_rad = H*30+30*M/60
m_rad = 6*M
theta = math.radians(abs(h_rad - m_rad))
ans = math.sqrt(A**2+B**2-2*A*B*math.cos(theta))

print(ans)