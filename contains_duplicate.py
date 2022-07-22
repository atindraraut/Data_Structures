from collections import Counter
class Solution:
    def containsDuplicate(nums):
        #using hash map
        val = Counter(nums)
        for i in val:
            if val[i]>1:
                return True
        return False
arrnum = [1,2,3,1]
print(Solution.containsDuplicate(arrnum))