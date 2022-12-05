N = int(input())

ans = []
def dfs(num):
  l = ['7', '5', '3']
  for i in l:
    n_num = i + num
    if int(n_num) <= N:
      if n_num.count('7')>=1 and n_num.count('5')>=1 and n_num.count('3')>=1:
        ans.append(n_num)
      dfs(n_num)

dfs('')
print(len(ans))