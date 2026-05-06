INF = 9999

def distance_vector(n, cost):
    dist = [row[:] for row in cost]
    next_hop = [[-1]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if cost[i][j] != INF and i != j:
                next_hop[i][j] = j

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_hop[i][j] = next_hop[i][k]

    for i in range(n):
        print(f"\nRouter {i+1} Table:")
        print("Dest\tNextHop\tDist")
        for j in range(n):
            print(j+1, next_hop[i][j]+1, dist[i][j], sep="\t")


n = 4
cost = [
    [0,1,3,INF],
    [1,0,1,INF],
    [3,1,0,4],
    [INF,INF,4,0]
]

distance_vector(n, cost)
