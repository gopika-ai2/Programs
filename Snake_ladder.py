# Python program to find minimum number of dice throws
# in Snakes and Ladders using BFS
from collections import deque

# Function to find the minimum number of dice throws
def getMinDiceThrows(move):
    n = len(move)
    visited = [False] * n
    q = deque()

    visited[0] = True

    # Start from cell 0 with 0 moves
    q.append([0, 0])

    while q:
        curr = q[0]
        v = curr[0]
        dist = curr[1]

        if v == n - 1:
            return dist

        q.popleft()

        # Try all possible dice throws from current cell
        for j in range(v + 1, min(v + 7, n)):
            if not visited[j]:
                visited[j] = True

                # Move to destination cell if 
                # there's a ladder/snake
                dest = move[j] if move[j] != -1 else j
                q.append([dest, dist + 1])

    return -1

if __name__ == "__main__":
    n = 30
    moves = [-1] * n

    # Ladders
    moves[2] = 21
    moves[4] = 7
    moves[10] = 25
    moves[19] = 28

    # Snakes
    moves[26] = 0
    moves[20] = 8
    moves[16] = 3
    moves[18] = 6

    print(getMinDiceThrows(moves))
