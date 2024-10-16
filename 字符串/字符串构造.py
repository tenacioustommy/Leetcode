# 小欧有一个字符串  s ，她想构造一个长度为  k 的字符串 t ，
# 使得 s+t 或 t+s 拼成的字符串是回文串。
s="qriq"
k=2
if len(s)==k:
    print(s[::-1])
    exit()
total_len=len(s)+k
huiwen_len=0
if total_len%2==1:
    huiwen_len=total_len//2
else:
    huiwen_len=total_len//2

res=""
for i in range(total_len-huiwen_len,len(s)):
    if s[i]!=s[total_len-i-1]:
        break
    if i==len(s)-1:
        res=s[:k][::-1]
        break
for  i in range(huiwen_len-k):
    if s[i]!=s[total_len-2*k-i-1]:
        break
    if i==huiwen_len-k-1:
        res=s[-k:][::-1]
        break
if res=="":
    print(-1)
else:
    print(res)

    
