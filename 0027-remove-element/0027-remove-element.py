class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        c = 0 
        for index in nums[:]:
            if index == val:
                nums.remove(index)
                c += 1
            else:
                pass

        return len(nums)


