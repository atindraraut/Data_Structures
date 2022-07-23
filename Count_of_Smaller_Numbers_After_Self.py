from sortedcontainers import SortedList
class Solution:
    def countSmaller(nums):
        s=SortedList()
        output = []
        for n in nums[::-1]:
            print(s)
            print(n)
            ans = SortedList.bisect_left(s,n)
            output.append(ans)
            s.add(n)
        return reversed(output)
               
print(Solution.countSmaller([2,1,1,0]))