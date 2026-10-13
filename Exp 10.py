def astar(graph, heuristic, start, goal):
    open_list = [(heuristic[start], 0, start, [start])]
    visited = set()

    while open_list:
        open_list.sort()
        f, g, node, path = open_list.pop(0)

        if node == goal:
            return path, g

        if node in visited:
            continue
        visited.add(node)

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                open_list.append((new_f, new_g, neighbor,
                                  path + [neighbor]))

    return None, float('inf')


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('E', 1)],
    'D': [('G', 3)],
    'E': [('G', 2)],
    'G': []
}

heuristic = {'A': 5, 'B': 4, 'C': 2, 'D': 3, 'E': 1, 'G': 0}

path, cost = astar(graph, heuristic, 'A', 'G')

print("Path:", path)
print("Total Cost:", cost)
