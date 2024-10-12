s="()(())"
# dp[i]设为到该位置结束的最长字串
dp=[0 for _ in range(len(s))]
for i in range(1,len(s)):
    if s[i]==')':
        if s[i-1]=='(':
            dp[i]=dp[i-2]+2
        elif s[i-1]==')' and i-dp[i-1]-1>=0 and s[i-dp[i-1]-1]=='(':
            dp[i]=dp[i-1]+2
            # 若前面还有括号对，加上前面的括号对
            if(i-dp[i-1]-2>=0):
                dp[i]+=dp[i-dp[i-1]-2]
        else:
            dp[i]=0
    elif s[i]=='(':
        dp[i]=0
print(max(dp))