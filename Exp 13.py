def minimax(depth, node, maximizing, values, max_depth):
    if depth == max_depth:
        return values[node]

    if maximizing:
        best = float('-inf')
        for i in range(2):
            val = minimax(depth + 1, node * 2 + i,
                          False, values, max_depth)
            best = max(best, val)
        return best
    else:
        best = float('inf')
        for i in range(2):
            val = minimax(depth + 1, node * 2 + i,
                          True, values, max_depth)
            best = min(best, val)
        return best


values = [3, 5, 2, 9, 12, 5, 23, 23]
max_depth = 3

result = minimax(0, 0, True, values, max_depth)
print("The optimal value is:", result)
