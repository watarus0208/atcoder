N, K = map(int, input().split())
X = list(map(int, input().split()))

dist = 0
k = 0
fire = [1]*N
ans = []
side = ''
turn = 0
i_max = len(X)
i_min = 0

def dfs(i, dist, k, fire, side, turn):
  if k==K:
    ans.append(dist)
  else:
    if i+1<i_max:
      if side == 'left':
        turn += 1
      if turn <= 1:
        if fire[i+1] == 1:
          fire[i+1] = 0
          k += 1
        dist += abs(X[i+1]-X[i])
        dfs(i+1, dist, k, fire, 'right', turn)
    if i-1>=i_min:
      if side == 'right':
        turn += 1
      if turn <= 1:
        if fire[i-1] == 1:
          fire[i-1] = 0
          k += 1
        dist += abs(X[i-1]-X[i])
        dfs(i-1, dist, k, fire, 'left', turn)
      
if 0 in X:
  dfs(0, 0, 1, fire, '', 0)
else:
  for j in range(N):
    if X[j]<0 and 0<X[j+1]:
      l_fire = [1]*N
      r_fire = [1]*N
      l_fire[j] = 0
      #print(l_fire)
      r_fire[j+1] = 0
      #print(r_fire)
      dfs(j, abs(X[j]), 1, l_fire, 'left', 0)
      dfs(j+1, abs(X[j+1]), 1, r_fire, 'right', 0)
  else:
    if min(X)>0:
      m_fire = [1]*N
      m_fire[0] = 0
      dfs(0, X[0], 1, m_fire, 'right', 0)
    if max(X)<0:
      m_fire = [1]*N
      m_fire[N-1] = 0
      dfs(X.index(N-1), 1, m_fire, 'left', 0)
#print(ans)
print(min(ans))