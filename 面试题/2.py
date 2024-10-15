import random
def simulate():
    sum1=0
    sum2=0
    # 第一个人succeed
    for _ in range(8):
        sum1+= random.randint(1,6)
        sum2+= random.randint(1,6)
        if sum1%10==0 :
            return True
        if sum2%10==0 :
            return False
    return False
def estimate(n):
    total=n
    count=0
    for _ in range(total):
        if simulate():
            count+=1
    return count/total

if __name__ == '__main__':
    print(estimate(1000000))
        
