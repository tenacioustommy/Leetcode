nums=[3,2,1,0,4]
def canJump(nums):
    max_dis=0
    for i in range(len(nums)):
        if i==len(nums)-1:
            return True
        if nums[i]!=0:
            tmp=i+nums[i]
            max_dis=max(tmp,max_dis)
        else:
            if i>=max_dis:
                return False
print(canJump(nums))