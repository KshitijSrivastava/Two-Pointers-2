
## Problem3 (https://leetcode.com/problems/search-a-2d-matrix-ii/)

"""
Space Complexity: O(1)
Time Complexity: O(M + N)
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nrows = len(matrix)
        ncols = len(matrix[0])
        
        i = 0                               #point to the top right corner
        j = ncols - 1
        
        while i <= nrows - 1 and j >= 0:    #while the pointer is inside the matrix
            if matrix[i][j] == target:      #if the matrix valeu at pointer is equal to target
                return True
            elif matrix[i][j] < target:     #if the matrix valeu at pointer is less than to target
                i += 1                      #increase the row number
            else:                           #if the matrix valeu at pointer is more than target
                j -= 1                      #decrease the column number
                
        return False