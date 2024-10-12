nums=[1,1,2,2]
nums.sort()
ans = []
path = []
visited = [0 for _ in range(len(nums))]
n = len(nums)
def dfs(i: int) -> None:
    if i == n:  # 子集构造完毕
        ans.append(path.copy())  # 复制 path
        return
    # 若重复，只能跳过
    if i > 0 and nums[i] == nums[i - 1] and visited[i - 1] == 0:
        dfs(i + 1)
        return
    # 不选 nums[i]
    dfs(i + 1)
    # 选 nums[i]
    path.append(nums[i])
    visited[i] = 1
    dfs(i + 1)
    path.pop()  # 恢复现场
    visited[i] = 0
dfs(0)
print(ans)
