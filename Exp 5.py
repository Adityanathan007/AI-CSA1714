from collections import deque

def solve():
    start = (3, 3, 1)
    goal = (0, 0, 0)
    moves = [(1, 0), (2, 0), (0, 1),
             (0, 2), (1, 1)]

    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()
        m, c, boat = state

        if state == goal:
            for step in path + [state]:
                print(step)
            return

        for dm, dc in moves:
            if boat == 1:
                new = (m-dm, c-dc, 0)
            else:
                new = (m+dm, c+dc, 1)

            nm, nc, _ = new

            if not (0 <= nm <= 3 and 0 <= nc <= 3):
                continue
            if nm > 0 and nm < nc:
                continue
            if 3-nm > 0 and 3-nm < 3-nc:
                continue

            if new not in visited:
                visited.add(new)
                queue.append((new, path + [state]))

solve()
