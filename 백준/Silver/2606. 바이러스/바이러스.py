num_computers = int(input())
num_connections = int(input())

graph = [[] for _ in range(num_computers + 1)]
for _ in range(num_connections):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (num_computers + 1)
stack = [1]
infected_count = 0

while stack:
    current = stack.pop()
    if not visited[current]:
        visited[current] = True
        infected_count += 1
        for neighbor in graph[current]:
            if not visited[neighbor]:
                stack.append(neighbor)

print(infected_count - 1)