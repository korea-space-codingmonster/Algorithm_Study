from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

print(graph)

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0
print(distance)

q = deque([x])
print(q)
while q:
  now = q.popleft()
  print(now)
  for next_node in graph[now]:
    if distance[next_node] == -1:
      distance[next_node] = distance[now] + 1
      q.append(next_node)

check = False
for i in range(1, n + 1):
  if distance[i] == k:
    print(i)
    check = True



