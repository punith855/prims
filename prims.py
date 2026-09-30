import heapq

def prims(n, edges, start):
    graph = [[] for _ in range(n + 1)]

    # Build adjacency list
    for u, v, w in edges:
        graph[u].append((w, v))
        graph[v].append((w, u))

    visited = [False] * (n + 1)
    min_heap = [(0, start)]
    total = 0

    while min_heap:
        weight, node = heapq.heappop(min_heap)

        if visited[node]:
            continue

        visited[node] = True
        total += weight

        # Add all edges from this node
        for next_weight, next_node in graph[node]:
            if not visited[next_node]:
                heapq.heappush(min_heap, (next_weight, next_node))

    return total


# Input
n, m = map(int, input().split())

edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

start = int(input())

print(prims(n, edges, start))