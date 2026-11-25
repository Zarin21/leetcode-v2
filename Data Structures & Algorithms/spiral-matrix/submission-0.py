class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix) - 1

        left = 0
        right = len(matrix[0]) - 1

        res = []

        while top <= bottom and left <= right:
            
            for _ in range(left, right + 1):
                res.append(matrix[top][_])
            top += 1

            for _ in range(top, bottom + 1):
                res.append(matrix[_][right])
            right -= 1

            if top <= bottom:
                for _ in range(right, left - 1, -1):
                    res.append(matrix[bottom][_])
                bottom -= 1
            if left <= right:
                for _ in range(bottom, top - 1, -1):
                    res.append(matrix[_][left])
                left += 1
        
        return res