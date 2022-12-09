from copy import copy
import numpy as np

with open('Day 9/input.txt') as f:
    lines = f.read().splitlines()

def doMoves(instructions):
    marked_grid = np.zeros((500, 500))
    H = [249, 249]
    T = [249, 249]
    marked_grid[T[0], T[1]] = 1
    for moves in instructions:
        if moves[0] == 'R':
            for step in range(int(moves[1::])):
                H[1] += 1
                if H[1] - T[1] == 2 and H[0] == T[0]:
                    T[1] += 1
                    marked_grid[T[0], T[1]] += 1
                elif H[1] - T[1] == 2 and H[0] - T[0] == 1:
                    T[1] += 1
                    T[0] += 1
                    marked_grid[T[0], T[1]] += 1
                elif H[1] - T[1] == 2 and T[0] - H[0] == 1:
                    T[1] += 1
                    T[0] -= 1
                    marked_grid[T[0], T[1]] += 1
                    
        elif moves[0] == 'L':
            for step in range(int(moves[1::])):
                H[1] -= 1
                if T[1] - H[1] == 2 and H[0] == T[0]:
                    T[1] -= 1
                    marked_grid[T[0], T[1]] += 1
                elif T[1] - H[1] == 2 and H[0] - T[0] == 1:
                    T[1] -= 1
                    T[0] += 1
                    marked_grid[T[0], T[1]] += 1
                elif T[1] - H[1] == 2 and T[0] - H[0] == 1:
                    T[1] -= 1
                    T[0] -= 1
                    marked_grid[T[0], T[1]] += 1
        elif moves[0] == 'U':
            for step in range(int(moves[1::])):
                H[0] -= 1
                if T[0] - H[0] == 2 and H[1] == T[1]:
                    T[0] -= 1
                    marked_grid[T[0], T[1]] += 1
                elif T[0] - H[0] == 2 and H[1] - T[1] == 1:
                    T[1] += 1
                    T[0] -= 1
                    marked_grid[T[0], T[1]] += 1
                elif T[0] - H[0] == 2 and T[1] - H[1] == 1:
                    T[1] -= 1
                    T[0] -= 1
                    marked_grid[T[0], T[1]] += 1
                
        else:
            for step in range(int(moves[1::])):
                H[0] += 1
                if H[0] - T[0] == 2 and H[1] == T[1]:
                    T[0] += 1
                    marked_grid[T[0], T[1]] += 1
                elif H[0] - T[0] == 2 and H[1] - T[1] == 1:
                    T[1] += 1
                    T[0] += 1
                    marked_grid[T[0], T[1]] += 1
                elif H[0] - T[0] == 2 and T[1] - H[1] == 1:
                    T[1] -= 1
                    T[0] += 1
                    marked_grid[T[0], T[1]] += 1
                
    return marked_grid

marked = doMoves(lines)

print(len(np.where(marked > 0)[0]))

# Second star

def checkConditions(H, T):
    if H[1] - T[1] == 2 and H[0] == T[0]:
        T[1] += 1
    elif H[1] - T[1] == 2 and H[0] - T[0] == 1:
        T[1] += 1
        T[0] += 1
    elif H[1] - T[1] == 2 and T[0] - H[0] == 1:
        T[1] += 1
        T[0] -= 1
    elif T[1] - H[1] == 2 and H[0] == T[0]:
        T[1] -= 1
    elif T[1] - H[1] == 2 and H[0] - T[0] == 1:
        T[1] -= 1
        T[0] += 1
    elif T[1] - H[1] == 2 and T[0] - H[0] == 1:
        T[1] -= 1
        T[0] -= 1
    elif T[0] - H[0] == 2 and H[1] == T[1]:
        T[0] -= 1
    elif T[0] - H[0] == 2 and H[1] - T[1] == 1:
        T[1] += 1
        T[0] -= 1
    elif T[0] - H[0] == 2 and T[1] - H[1] == 1:
        T[1] -= 1
        T[0] -= 1
    elif H[0] - T[0] == 2 and H[1] == T[1]:
        T[0] += 1
    elif H[0] - T[0] == 2 and H[1] - T[1] == 1:
        T[1] += 1
        T[0] += 1
    elif H[0] - T[0] == 2 and T[1] - H[1] == 1:
        T[1] -= 1
        T[0] += 1
    elif H[0] - T[0] == 2 and H[1] - T[1] == 2:
        T[1] += 1
        T[0] += 1
    elif H[0] - T[0] == 2 and T[1] - H[1] == 2:
        T[1] -= 1
        T[0] += 1
    elif T[0] - H[0] == 2 and T[1] - H[1] == 2:
        T[1] -= 1
        T[0] -= 1
    elif T[0] - H[0] == 2 and H[1] - T[1] == 2:
        T[1] += 1
        T[0] -= 1
    
    
    return H, T


def do10Moves(instructions):
    marked_grid = np.zeros((500, 500))
    h = [249, 249]
    t = [249, 249]
    T = [copy(h), copy(t), copy(t), copy(t), copy(t), copy(t), copy(t), copy(t), copy(t), copy(t)]
    marked_grid[h[0], h[1]] = 9
    for moves in instructions:
        if moves[0] == 'R':
            for step in range(int(moves[1::])):
                T[0][1] += 1
                for knot in range(len(T)-1):
                    T[knot], T[knot+ 1] = checkConditions(T[knot], T[knot+ 1])
                    if knot+1 == 9:
                        marked_grid[T[knot+1][0], T[knot+1][1]] = knot+1
                    
        elif moves[0] == 'L':
            for step in range(int(moves[1::])):
                T[0][1] -= 1
                for knot in range(len(T)-1):
                    T[knot], T[knot+ 1] = checkConditions(T[knot], T[knot+ 1])
                    if knot+1 == 9:
                        marked_grid[T[knot+1][0], T[knot+1][1]] = knot+1
        elif moves[0] == 'U':
            for step in range(int(moves[1::])):
                T[0][0] -= 1
                for knot in range(len(T)-1):
                    T[knot], T[knot+ 1] = checkConditions(T[knot], T[knot+ 1])
                    if knot+1 == 9:
                        marked_grid[T[knot+1][0], T[knot+1][1]] = knot+1
                
        else:
            for step in range(int(moves[1::])):
                T[0][0] += 1
                for knot in range(len(T)-1):
                    T[knot], T[knot+ 1] = checkConditions(T[knot], T[knot+ 1])
                    if knot+1 == 9:
                        marked_grid[T[knot+1][0], T[knot+1][1]] = knot+1
                
    return marked_grid


ten_marked = do10Moves(lines)
print(len(np.where(ten_marked == 9)[0]))
