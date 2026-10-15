def solve_map_coloring(neighbors, colors):
    # Make the adjacency graph undirected.
    graph = {region: set() for region in neighbors}
    for region, adjacent_regions in neighbors.items():
        for adjacent in adjacent_regions:
            graph.setdefault(adjacent, set())
            graph[region].add(adjacent)
            graph[adjacent].add(region)

    domains = {region: set(colors) for region in graph}
    assignment = {}

    def backtrack():
        if len(assignment) == len(graph):
            return assignment.copy()

        # MRV: choose the unassigned region with the fewest available colors.
        unassigned = [r for r in graph if r not in assignment]
        region = min(
            unassigned,
            key=lambda r: (
                len(domains[r]),
                -sum(n not in assignment for n in graph[r]),
            ),
        )

        for color in list(domains[region]):
            if any(assignment.get(n) == color for n in graph[region]):
                continue

            assignment[region] = color
            old_domains = {r: d.copy() for r, d in domains.items()}
            failed = False

            # Forward checking: adjacent regions cannot use this color.
            for neighbor in graph[region]:
                if neighbor not in assignment:
                    domains[neighbor].discard(color)
                    if not domains[neighbor]:
                        failed = True
                        break

            if not failed:
                result = backtrack()
                if result is not None:
                    return result

            assignment.pop(region)
            domains.update(old_domains)

        return None

    return backtrack()


if __name__ == "__main__":
    australia = {
        "Western Australia": {"Northern Territory", "South Australia"},
        "Northern Territory": {"South Australia", "Queensland"},
        "South Australia": {"Queensland", "New South Wales", "Victoria"},
        "Queensland": {"New South Wales"},
        "New South Wales": {"Victoria"},
        "Victoria": set(),
        "Tasmania": set(),
    }

    colors = ["Red", "Green", "Blue"]
    solution = solve_map_coloring(australia, colors)

    if solution is None:
        print("No valid coloring found.")
    else:
        for region, color in sorted(solution.items()):
            print(f"{region}: {color}")
