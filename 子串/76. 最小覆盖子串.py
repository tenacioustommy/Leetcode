s = "cabwefgewcwaefgcf"
t = "cae"
# Output: "BANC"
target={i:0 for i in t}
for i in t:
    target[i]+=1
# dict={i:0 for i in t}
def ismatch():
    for i in target.values():
        if i>0:
            return False
    return True

def minWindow(s: str, t: str) -> str:
    i=0
    j=0
    minlen=10e5
    res=""
    while  j<len(s):
        if i<=j:
            if s[j] in t:
                target[s[j]]-=1
                if ismatch():
                    minlen=min(minlen,j-i+1)
                    if minlen==j-i+1:
                        res=s[i:j+1]
                    j+=1
                    while i<j:
                        if s[i] in t:
                            target[s[i]]+=1
                        i+=1
                        if ismatch():
                            minlen=min(minlen,j-i)
                            if minlen==j-i:
                                res=s[i:j]
                            
                        else:
                            break
                    continue     
                else:
                    j+=1
                # 不符合，继续j向右找符合的
            else:
                j+=1
        
    return res
print(minWindow(s,t))
