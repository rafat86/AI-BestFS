# Ra'fat Naserdeen

import heapq
import numpy as np
import random

# Define the board and obstacles
board = np.full((5, 5), 1)

ghost_pos = (random.randint(0, 4), random.randint(0, 4))
board[ghost_pos] = 3
obstacles = [ghost_pos]

PACman_pos = (random.randint(0, 4), random.randint(0, 4))

while PACman_pos == ghost_pos:
    PACman_pos = (random.randint(0, 4), random.randint(0, 4))

board[PACman_pos] = 2
start_pos = [PACman_pos]
start_point = start_pos[0]

print("PACman start at: ", start_point)
print("Ghost position is in: ", ghost_pos)
print("PACman has to move the following directions to reach the goal")


def heuristic():
    return np.count_nonzero(board == 1)


def best_first_search(start):
    heap = [(heuristic(), start)]
    visited = set()
    directions = []
    while heap:
        _, pos = heapq.heappop(heap)
        if pos in visited:
            continue
        visited.add(pos)
        i, j = pos
        if board[i, j] == 1:
            board[i, j] = 0
            if not np.any(board == 1):
                return
            if len(directions) > 0:
                last_i, last_j = directions[-1]
                if last_i == i:
                    if last_j < j:
                        print("Move right")
                    else:
                        print("Move left")
                else:
                    if last_i < i:
                        print("Move down")
                    else:
                        print("Move up")
            else:
                print("Start")
            directions.append(pos)
        for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= ni < 5 and 0 <= nj < 5 and board[ni, nj] != 3 and (ni, nj) not in visited:
                heapq.heappush(heap, (heuristic(), (ni, nj)))


best_first_search(start_point)
