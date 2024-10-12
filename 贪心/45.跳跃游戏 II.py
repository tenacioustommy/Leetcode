nums=[2,3,1,1,4]
maxpos=0
nextmaxpos=0
res=0
for i in range(len(nums)):
    if i>maxpos:
        maxpos=nextmaxpos
        res+=1
    nextmaxpos=max(nextmaxpos,i+nums[i])
    