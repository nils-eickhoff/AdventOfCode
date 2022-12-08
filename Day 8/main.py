import numpy as np 

with open ('Day 8/input.txt') as f:
    lines = f.read().splitlines()

outer_visible = (len(lines[0]) - 1) * 4

def strToInt(rows):
    matrix = np.zeros((len(rows), len(rows[0])))
    for i, row in enumerate(rows):
        for j, r in enumerate(row):
            matrix[i, j] = int(row[j])
    return matrix

# First star

def runInnerGrid(input_matrix):
    matrix = np.zeros((len(input_matrix), len(input_matrix[0])))
    for r in range(1, len(input_matrix)-1):
        for c in range(1, len(input_matrix[0,:])-1):
            if input_matrix[r, c] > np.max(input_matrix[r+1::, c]):
                matrix[r, c] = 1
            elif input_matrix[r, c] > np.max(input_matrix[0:r, c]):
                matrix[r, c] = 1
            elif input_matrix[r, c] > np.max(input_matrix[r, c+1::]):
                matrix[r, c] = 1
            elif input_matrix[r, c] > np.max(input_matrix[r, 0:c]):
                matrix[r, c] = 1
    return matrix
    

matrix = strToInt(lines)
visible_matrix = runInnerGrid(matrix)
print(np.sum(visible_matrix) + outer_visible)

# Second star
def runInnerScore(input_matrix):
    matrix = np.zeros((len(input_matrix), len(input_matrix[0])))
    for r in range(1, len(input_matrix)-1):
        for c in range(1, len(input_matrix[0,:])-1):
            down = 0
            for tree in input_matrix[r+1::, c]:
                if tree < input_matrix[r, c]:
                    down += 1
                else:
                    down += 1
                    break
            up = 0
            for tree in input_matrix[0:r, c][::-1]:
                if tree < input_matrix[r, c]:
                    up += 1
                else:
                    up += 1
                    break
            right = 0
            for tree in input_matrix[r, c+1::]:
                if tree < input_matrix[r, c]:
                    right += 1
                else:
                    right += 1
                    break
            left = 0
            for tree in input_matrix[r, 0:c][::-1]:
                if tree < input_matrix[r, c]:
                    left += 1
                else:
                    left += 1
                    break
            matrix[r, c] = down*up*right*left
    return matrix

score_matrix = runInnerScore(matrix)
print(np.max(score_matrix))
