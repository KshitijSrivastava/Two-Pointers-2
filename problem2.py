
## Problem2 (https://leetcode.com/problems/merge-sorted-array/)

"""
Time Complexity: O(m + n)
Space Complexity: O(1)
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i = m - 1                       #Ptr points to last elements of array
        j = n - 1
        k = m + n - 1                   #pointer to the last element of output array
        
        while i >= 0 and j >= 0:        #while both ptr inside the respective arrays
            if nums1[i] >= nums2[j]:    # if num1 element is bigger than num2
                nums1[k] = nums1[i]
                i -= 1                  #change the num1 ptr
            else:
                nums1[k] = nums2[j]     #change the num2 ptr
                j -= 1
            k -= 1
                
        while j >= 0:                   #add the left over elements of num1
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
            
        while i >= 0:                   #add the left over elemnts of the num2
            nums1[k] = nums1[i]
            i -= 1
            k -= 1
            
            
        