# 1以上N以下
# 7,5,3が必ず入る
 
def dfs(num, f3, f5, f7):
    if num > N: return 0
    res = 0
    if f3 and f5 and f7: res = 1
    res += dfs(num*10+7, f3, f5, 1)
    res += dfs(num*10+5, f3, 1, f7)
    res += dfs(num*10+3, 1, f5, f7)
    return res
 
N = int(input())
ans = dfs(0, 0, 0, 0)
print(ans)