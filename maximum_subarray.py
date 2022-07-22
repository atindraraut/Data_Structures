class Solution:
    def maxSubArray(nums):
        maxarr = nums[0]
        nsum = 0
        
        for i in nums:
            if nsum <0:
                nsum = 0
            nsum += i
            maxarr = max(maxarr,nsum)
        return maxarr
arrval = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution.maxSubArray(arrval))