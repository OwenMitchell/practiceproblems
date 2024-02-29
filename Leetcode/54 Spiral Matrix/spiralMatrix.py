class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        if len(matrix[0]) == 1:
            return [x[0] for x in matrix]
        if len(matrix) == 1:
            return matrix[0]
        else:
            newMatrix = matrix[1:]
            transposed_matrix = [[row[i] for row in newMatrix] for i in range(len(newMatrix[0])-1, -1, -1)]
            return matrix[0] + self.spiralOrder(transposed_matrix)
