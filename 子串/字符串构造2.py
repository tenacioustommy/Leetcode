s=input()
set_=set()
for i in range(len(s)):
    set_.add(s[i])
if len(set_)==1:
    print(-1)
else:
    res=[]
    for i in range(len(s)):
        list_set=list(set_)
        res.append(list_set[(list_set.index(s[i])+1)%len(list_set)])
    print(''.join(res))
