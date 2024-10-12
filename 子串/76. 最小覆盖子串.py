s = "ab"
t = "a"
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
    j=-1
    minlen=10e5
    res=""
    while i+len(t)<=len(s):
        if i+len(t)<=j:
            if s[i] in t:
                if ismatch():
                    minlen=min(minlen,j-i+1)
                    res=s[i:j+1]
                    target[s[i]]+=1
                    i+=1
                else:
                    target[s[i]]+=1
                    i+=1  
                if ismatch():
                    continue
                
            else:
                i+=1
                continue
        if j<len(s):
            j+=1
        while j<len(s):
            if s[j] in t:
                target[s[j]]-=1
                if ismatch():
                    minlen=min(minlen,j-i+1)
                    res=s[i:j+1]
                    break
            j+=1
    return res
print(minWindow(s,t))
