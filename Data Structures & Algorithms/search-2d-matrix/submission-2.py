class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        l = 0
        r = row - 1
        target_row = -1

        while l <= r:
            m = (l + (r - l) // 2) 
            if matrix[m][0] == target or matrix[m][col - 1] == target:
                return True
            elif matrix[m][0] < target and matrix[m][col - 1] > target:
                target_row = m
                break
            elif matrix[m][col - 1] < target:
                l = m + 1
            else:
                r = m - 1
        if target_row == -1:
            return False

        l = 0 
        r = col - 1
        
        while l <= r:
            m = (l + (r - l) // 2)
            if matrix[target_row][m] == target:
                return True
            elif matrix[target_row][m] < target:
                l = m + 1
            else:
                r = m - 1
        return False