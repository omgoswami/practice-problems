class Solution:
    def solve(self, matrix):
        if matrix:
            new_mat = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        else:
            return []
        return new_mat
