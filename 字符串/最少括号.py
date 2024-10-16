# 小欧拿到了一个只包含'('和')'的字符串，她有以下两种操作：
# 1. 用"("代替一对括号："()"。
# 2. 用")"代替一对括号："()"。
# 请注意，只有相邻的括号字符才可以操作。
# 小欧想知道，若干次操作以后，该字符串的最短长度是多少？
s=")()("
i=0
j=len(s)-1
while i<len(s)-1:
    if s[i]=="(":
        break
    i+=1
while j>0:
    if s[j]==")":
        break
    j-=1
if i>j:
    print(len(s))
    exit()
sum=i+len(s)-j
print(sum)
