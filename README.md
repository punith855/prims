# Prim's Algorithm - Minimum Spanning Tree

This is my Python solution for the **Prim's (MST): Special Subtree** problem on HackerRank.

The goal of the problem is to connect all the nodes in a weighted undirected graph with the minimum possible total edge weight.

## What I used

* Python
* Prim's Algorithm
* Adjacency List
* Min Heap using `heapq`

## How the solution works

I first store the graph using an adjacency list.

Starting from the given node, I use a min heap to keep track of the available edges. At every step, I take the edge with the smallest weight that leads to an unvisited node.

If the node has already been visited, I skip it.

I keep adding the selected edge weights until all the nodes are connected.

## Code

```python
import heapq

def prims(n, edges, start):
    graph = [[] for _ in range(n + 1)]

    # Create the adjacency list
    for u, v, w in edges:
        graph[u].append((w, v))
        graph[v].append((w, u))

    visited = [False] * (n + 1)

    # (weight, node)
    min_heap = [(0, start)]

    total = 0

    while min_heap:
        weight, node = heapq.heappop(min_heap)

        if visited[node]:
            continue

        visited[node] = True
        total += weight

        for next_weight, next_node in graph[node]:
            if not visited[next_node]:
                heapq.heappush(min_heap, (next_weight, next_node))

    return total


# Read input
n, m = map(int, input().split())

edges = []

for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

start = int(input())

print(prims(n, edges, start))
```

## Example

### Input

```text
5 6
1 2 3
1 3 4
4 2 6
5 2 2
2 3 5
3 5 7
1
```

### Edges selected

```text
1 - 2   = 3
2 - 5   = 2
1 - 3   = 4
2 - 4   = 6
```

Total:

```text
3 + 2 + 4 + 6 = 15
```

### Output

```text
15
```

## Complexity

For the adjacency list + min heap approach:

* Time: `O(E log E)`
* Space: `O(V + E)`

where `V` is the number of nodes and `E` is the number of edges.

## Problem

**HackerRank:** Prim's (MST): Special Subtree

## Language

Python 3

---

I'm using this problem to practice **graphs, greedy algorithms, priority queues, and heaps**.
