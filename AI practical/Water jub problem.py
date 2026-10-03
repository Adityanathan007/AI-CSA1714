from collections import deque

def water_jug(cap_a, cap_b, target):
    start = (0, 0)
    queue = deque([(start, [start])])
    seen = {start}

    while queue:
        (a, b), path = queue.popleft()

        if target in (a, b):
            return path

        pour_a_to_b = min(a, cap_b - b)
        pour_b_to_a = min(b, cap_a - a)

        next_states = [
            (cap_a, b), (a, cap_b),  # Fill
            (0, b), (a, 0),          # Empty
            (a - pour_a_to_b, b + pour_a_to_b),
            (a + pour_b_to_a, b - pour_b_to_a),
        ]

        for state in next_states:
            if state not in seen:
                seen.add(state)
                queue.append((state, path + [state]))

    return None

print(water_jug(4, 3, 2))
