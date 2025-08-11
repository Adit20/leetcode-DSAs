class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        c = 0 

        for i in nums[:]:
            if i == val:
                nums.remove(i)
                c += 1
            else:
                pass
            
        print(nums)