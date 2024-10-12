digits=""
ans = []
path = []
visited = [0 for _ in range(len(digits))]
n = len(digits)
dict={
    "2":["a","b","c"],
    "3":["d","e","f"],
    "4":["g","h","i"],
    "5":["j","k","l"],
    "6":["m","n","o"],
    "7":["p","q","r","s"],
    "8":["t","u","v"],
    "9":["w","x","y","z"]
}
def dfs(i: int) -> None:
    if i == n:  # 子集构造完毕
        ans.append(''.join(path[:]))  # 复制 path
        return
    # 选 digits[i]
    for j in dict[digits[i]]:
        path.append(j)
        dfs(i + 1)
        path.pop()
dfs(0)
print(ans)