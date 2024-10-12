input=input()
input_list=eval(input)
input_list.sort()
visited=[0 for _ in range(len(input_list))]
path=[]
res=[]
def dfs():
    if len(path)==len(input_list):
        res.append(path[:])
    for i in range(len(input_list)):
        if i>0 and visited[i-1]==0   and input_list[i]==input_list[i-1]:
            continue
        if visited[i]==0 :
            path.append(input_list[i])
            visited[i]=1
            dfs()
            path.pop()
            visited[i]=0
dfs()
print(res)
            

