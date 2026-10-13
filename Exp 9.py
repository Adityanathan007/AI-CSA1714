def tsp(graph, start):
    n = len(graph)
    visited = [start]
    cost = 0
    current = start

    while len(visited) < n:
        next_city = min(
            (city for city in range(n) if city not in visited),
            key=lambda city: graph[current][city]
        )
        cost += graph[current][next_city]
        visited.append(next_city)
        current = next_city

    cost += graph[current][start]
    visited.append(start)

    print("Path:", visited)
    print("Total Cost:", cost)

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

tsp(graph, 0)
