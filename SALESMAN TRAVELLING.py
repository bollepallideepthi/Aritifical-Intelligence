import itertools

# Distance matrix (symmetric graph)
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

def travelling_salesman(graph, start=0):
    n = len(graph)
    cities = range(n)
    min_path = None
    min_cost = float("inf")

    for perm in itertools.permutations(cities):
        if perm[0] == start:  # start from given city
            cost = 0
            for i in range(n - 1):
                cost += graph[perm[i]][perm[i+1]]
            cost += graph[perm[-1]][start]  # return to start
            if cost < min_cost:
                min_cost = cost
                min_path = perm
    return min_path, min_cost

path, cost = travelling_salesman(graph)
print("Best Path:", path)
print("Minimum Cost:", cost)
