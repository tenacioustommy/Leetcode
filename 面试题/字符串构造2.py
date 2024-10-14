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
        if s[i]==list_set[0]:
            res.append(list_set[1])
        else:
            res.append(list_set[0]         )
    print(''.join(res))
