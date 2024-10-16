# 定义一个排列为“好排列”，当且仅当所有相邻两个数的乘积均为偶数。
# 小欧想知道，长度
# n
# n的好排列一共有多少种？由于该数可能过大，请对
# 1
# 0
# 9
# +
# 7
# 10 
# 9
#  +7取模。
n=int(input())
N=10**9+7
# print(N)
mul=1
def get(x):
    mul=1
    for i in range(1,x//2+1):
        mul=(mul*i)%N
    mul=(2*mul*mul)%N
    return mul
if n%2==1:
    for i in range(1,(n+1)//2):
        mul=(mul*i)%N
    mul=((n+1)//2*mul*mul)%N
    print(int(mul))
else:
    if n==2:
        print(2)
        exit()
    dp=[0 for _ in range(n//2+1)]
    dp[0] =0
    dp[1]=0
    dp[2]=4
    for i in range(3,n//2+1):
        dp[i] = (dp[i-2]+get(2*i-4))*i*(i-1)*i*(i-1)%N
    print(int((dp[n//2]+get(n))%N))
        
        