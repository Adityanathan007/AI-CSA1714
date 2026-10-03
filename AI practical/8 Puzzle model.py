from collections import deque

def bfs(start, goal):
    start, goal = tuple(start), tuple(goal)
    queue = deque([(start, [start])])
    seen = {start}

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path

        i = state.index(0)
        row, col = divmod(i, 3)

        for r, c in ((row-1, col), (row+1, col),
                     (row, col-1), (row, col+1)):
            if 0 <= r < 3 and 0 <= c < 3:
                j = r * 3 + c
                next_state = list(state)
                next_state[i], next_state[j] = next_state[j], next_state[i]
                next_state = tuple(next_state)

                if next_state not in seen:
                    seen.add(next_state)
                    queue.append((next_state, path + [next_state]))

start = [1, 2, 3, 4, 0, 6, 7, 5, 8]  # 0 is the blank
goal  = [1, 2, 3, 4, 5, 6, 7, 8, 0]

print(bfs(start, goal))
