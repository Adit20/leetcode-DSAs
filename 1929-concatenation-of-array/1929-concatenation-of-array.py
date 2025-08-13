class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sList = []
       
        sList[:] = nums

        nList = nums + sList

        return nList
        