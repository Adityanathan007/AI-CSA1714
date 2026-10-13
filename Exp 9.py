from itertools import permutations

cost = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(cost)
min_cost = float('inf')

for path in permutations(range(1, n)):
    route = (0,) + path + (0,)
    total = sum(cost[route[i]][route[i+1]]
                for i in range(n))

    if total < min_cost:
        min_cost = total
        best_route = route

print("Best Route:", best_route)
print("Minimum Cost:", min_cost)
