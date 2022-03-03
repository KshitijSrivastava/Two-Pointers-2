
## Problem1 (https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)



class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)                               #count the number of elements
        k = 0                                       #outputPtr
        
        i = 0                                       #unique number iterator
        
        while i < n:
            
            j = i                                   #comparing iterator
            while j < n and nums[j] == nums[i]:     #continue till both pointer are not equal
                if i == j or i + 1 == j:            #if both elements are 0 or two index apart
                    nums[k] = nums[i]
                    k += 1                          #advance the output index ptr
                j += 1                              #advance the jth ptr
            i = j                                   #advance the ith ptr to new number
        return k