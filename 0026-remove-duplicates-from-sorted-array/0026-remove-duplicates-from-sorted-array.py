class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique = sorted(set(nums))
        nums[:] = unique
        return len(unique)

        
        
        