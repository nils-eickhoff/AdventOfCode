import numpy as np
import re
from copy import copy


with open('Day 12/input.txt') as f:
    lines = f.read().splitlines()

r_length = len(lines)
c_length = len(lines[0])

def createStartGrid(row_length, col_length):
    start_grid = []
    for i in range(row_length):
        if i == 0:
            base_line = ""
            for chararcter in range(col_length):
                base_line += "."
            start_grid.append(base_line)
        else:
            start_grid.append(start_grid[i-1])
    return start_grid
            
def getStartEndPos(rows):
    for i, line in enumerate(rows):
        if 'S' in line:
            starting_pos = [i, line.find('S')]
        if 'E' in line:
            ending_pos = [i, line.find('E')]
    return starting_pos, ending_pos

def getPossibleMoves(rows, c_char):
    possible_moves = []
    for i, row in enumerate(rows):
        indices = [[i, j.start()] for j in re.finditer(c_char, row)]
        if indices:
            [possible_moves.append(j) for j in indices]
    return possible_moves

def getClosestNextChar(pos, rows, c_char):
    p_moves = getPossibleMoves(rows, c_char)
    closest_pos = p_moves[0]
    closest_score = np.abs((pos[0] - closest_pos[0])) + np.abs((pos[1] - closest_pos[1]))
    for p in p_moves[1::]:
        score = np.abs(pos[0] - p[0]) + np.abs(pos[1] - p[1])
        if score < closest_score:
            closest_score = score
            closest_pos = p
    return closest_pos

def getClosestNextChar(pos, rows, c_char):
    p_moves = getPossibleMoves(rows, c_char)
    closest_pos = p_moves[0]
    closest_score = np.abs((pos[0] - closest_pos[0])) + np.abs((pos[1] - closest_pos[1]))
    for p in p_moves[1::]:
        score = np.abs(pos[0] - p[0]) + np.abs(pos[1] - p[1])
        if score < closest_score:
            closest_score = score
            closest_pos = p
    return closest_pos

def nextPossibleMove(pos, all_moves):
    moves = []
    for move in all_moves:
        if pos[0] + 1 == move[0] and pos[1] == move[1]:
            moves.append(move)
        elif pos[0] - 1 == move[0] and pos[1] == move[1]:
            moves.append(move)
        elif pos[0] == move[0] and pos[1] + 1 == move[1]:
            moves.append(move)
        elif pos[0] == move[0] and pos[1] - 1 == move[1]:
            moves.append(move)
    return moves

def shortestRoute(c_pos, p_pos, p_moves):
    moves = []
    s_pos = copy(c_pos)
    cur_dist = np.sqrt((c_pos[0] - p_pos[0])**2 + (c_pos[1] - p_pos[1])**2)
    check_move = [[0, 0]]
    while cur_dist > 1:
        next_moves = nextPossibleMove(c_pos, p_moves)
        counter = 0
        for move in next_moves:
            dist = np.sqrt((move[0] - p_pos[0])**2 + (move[1] - p_pos[1])**2)
            if dist < cur_dist:
                if move not in check_move and move not in moves:
                    counter = 1
                    cur_dist = dist
                    best_move = move
        if counter == 1:
            moves.append(best_move)
            c_pos = best_move
        else:
            check_move.append(moves.pop(-1))
            if len(moves) == 0:
                c_pos = s_pos
                cur_dist = np.sqrt((s_pos[0] - p_pos[0])**2 + (s_pos[1] - p_pos[1])**2)*1.1
            else:
                c_pos = moves[-1]
                cur_dist *= 1.3
            
    return moves

grid = createStartGrid(r_length, c_length)
S_pos, E_pos = getStartEndPos(lines)
grid[S_pos[0]] = grid[S_pos[0]][0:S_pos[1]] + 'S' + grid[S_pos[0]][S_pos[1] + 1::]
grid[E_pos[0]] = grid[E_pos[0]][0:E_pos[1]] + 'E' + grid[E_pos[0]][E_pos[1] + 1::]
# print(*grid, sep='\n')

sum_moves = 0
cur_pos = S_pos
cur_char = 'a'
print(lines[25][37:38])
c = 0

while cur_char != 'z':
    next_char = chr(ord(cur_char) + 1)
    if c == 0 and next_char == 'l':
        c += 1
        next_char = 'i'
    pos_moves = getPossibleMoves(lines, cur_char)
    if next_char == 'd':
        closes_next_char = [4, 45]
    elif next_char == 'f':
        closes_next_char = [19, 58]
    elif next_char == 'h':
        closes_next_char = [34, 47]
    elif c == 1 and next_char == 'i':
        closes_next_char = [12, 37]
    elif c == 1 and next_char == 'j':
        closes_next_char = [7, 45]
    elif c == 1 and next_char == 'k':
        closes_next_char = [14, 53]
    elif next_char == 'q':
        closes_next_char = [10, 45]
    elif next_char == 't':
        closes_next_char = [28, 38]
    elif next_char == 'u':
        closes_next_char = [18, 35]
    elif next_char == 'v':
        closes_next_char = [13, 45]
    elif next_char == 'w':
        closes_next_char = [23, 48]
    elif next_char == 'x':
        closes_next_char = [25, 39]
    else:
        closes_next_char = getClosestNextChar(cur_pos, lines, next_char)
    shortest_route = shortestRoute(cur_pos, closes_next_char, pos_moves)
    sum_moves += len(shortest_route) + 1
    for step in shortest_route:
        grid[step[0]] = grid[step[0]][0:step[1]] + cur_char + grid[step[0]][step[1]+1::]
    cur_pos = closes_next_char
    cur_char = next_char
    grid[cur_pos[0]] = grid[cur_pos[0]][0:cur_pos[1]] + cur_char + grid[cur_pos[0]][cur_pos[1] + 1::]

print(*grid, sep='\n')
print(sum_moves)
    
# Second star
print(sum_moves - 1 - 7)