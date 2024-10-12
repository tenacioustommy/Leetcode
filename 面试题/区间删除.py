# 小美拿到了一个大小为n的数组，她希望删除一个区间后，使得剩余所有元素的乘积末尾至少有k个 0。小美想知道，一共有多少种不同的删除方案？
# n,k=map(int,input().split())
# input_list=list(map(int,input().split()))
n,k=10,2
input_list=[6,7,3,4,4,5,10,2,10,6]
factor2_list=[0 for _ in range(n)]
factor5_list=[0 for _ in range(n)]
def get_factor_num(x,factor):
    if x==0:
        return 0
    if x % factor == 0:
        return get_factor_num(x // factor, factor) + 1
    else:
        return 0
factor2_list = list(map(lambda x: get_factor_num(x, 2), input_list))
factor5_list = list(map(lambda x: get_factor_num(x, 5), input_list))

i=0
j=0
res=0
cur_2=cur_5=0
sum_2=sum(factor2_list)
sum_5=sum(factor5_list)
while i<n and j<=n :
    if i<j:
        if j<n and sum_2-cur_2-factor2_list[j]>=k and sum_5-cur_5-factor5_list[j]>=k :     
            cur_2+=factor2_list[j]
            cur_5+=factor5_list[j]   
            j+=1
        else:
            res+=j-i
            cur_2-=factor2_list[i]
            cur_5-=factor5_list[i]
            i+=1
    # 同时移ii且cur为空
    elif i==j:
        # 有足够0的情况
        if sum_2-factor2_list[j]>=k and sum_5-factor5_list[j]>=k:
            cur_2+=factor2_list[j]
            cur_5+=factor5_list[j]
            j+=1
        else:
            i+=1
            j+=1        
print(res)
    
    
