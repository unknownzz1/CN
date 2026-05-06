INF = 9999

def dijkstra(n, cost, src):
    dist = [INF]*n
    visited = [False]*n
    parent = [-1]*n

    dist[src] = 0

    for _ in range(n-1):
        u = min((i for i in range(n) if not visited[i]), key=lambda i: dist[i])
        visited[u] = True

        for v in range(n):
            if not visited[v] and cost[u][v] != INF and dist[u] + cost[u][v] < dist[v]:
                dist[v] = dist[u] + cost[u][v]
                parent[v] = u

    # Find next hop
    next_hop = [-1]*n
    for i in range(n):
        if i == src or parent[i] == -1:
            continue
        j = i
        while parent[j] != src:
            j = parent[j]
        next_hop[i] = j

    return dist, next_hop


# Example graph (same style as your C code)
n = 4
cost = [
    [0,1,3,INF],
    [1,0,1,INF],
    [3,1,0,4],
    [INF,INF,4,0]
]

# Routing table for each router
for i in range(n):
    print(f"\nRouter {i+1} Table:")
    print("Dest\tNextHop\tDist")
    dist, nh = dijkstra(n, cost, i)
    for j in range(n):
        print(j+1, nh[j]+1, dist[j], sep="\t")
