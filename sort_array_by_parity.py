# https://leetcode.com/problems/sort-array-by-parity/


class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even = []
        odd = []
        
        for value in A:
            if value % 2 == 0:
                even.append(value)
            else:
                odd.append(value)
        
        return even + odd

"""
Provided Solution

class Solution(object):
    def sortArrayByParity(self, A):
        A.sort(key = lambda x: x % 2)
        return A

_Learnings | Use a custom comparator when sorting, to sort by parity.
"""
        
 
