nums=[1,2,3,4,5,6,7]
k=2
n=len(nums)
k = k % n
nums[:] = nums[-k:] + nums[:-k]