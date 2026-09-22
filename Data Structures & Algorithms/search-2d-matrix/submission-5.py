class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Find the last row whose first element <= target
        start = 0
        end = len(matrix)

        while start < end:
            mid = start + (end - start) // 2

            if matrix[mid][0] <= target:
                start = mid + 1
            else:
                end = mid

        row = start - 1

        if row < 0:
            return False

        # Binary search within the candidate row
        start = 0
        end = len(matrix[row])

        while start < end:
            mid = start + (end - start) // 2

            if matrix[row][mid] < target:
                start = mid + 1
            elif matrix[row][mid] > target:
                end = mid
            else:
                return True

        return False
