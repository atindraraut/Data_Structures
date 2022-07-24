#Search_a_2D_Matrix_II
class Solution:
    def searchMatrix(matrix, target):
        r=0
        c = len(matrix[0])-1
        while(r<len(matrix) and c>=0):
            if(matrix[r][c] == target):
                return True
            elif(matrix[r][c]<target):
                r+=1
            else:
                c = c-1
        return False
matrix = [[1,1]]
target = 5
print(Solution.searchMatrix(matrix,target))