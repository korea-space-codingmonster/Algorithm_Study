#탐색이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정을 말합니다.
#대표족인 그래프 탐색 알고리즘으로는 DFS BFS가 있다

#스택 : 먼저들어온 데이터가 나중에 나가는 형식(선입후출) 자료구조
# 입구와 출구가 동일한 형태로 시각화할 수 있다.

#삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
#5237
#523
#5231
#52314
#5231

#파이썬에서 append()로 넣고 pop()으로 삭제 가능

# stack = []
# stack.append(5)
# stack.append(2)
# stack.append(3)
# stack.append(7)
# stack.pop()
# stack.append(1)
# stack.append(4)
# stack.pop()

# print(stack[::-1])#최상단 원소부터 출력
# print(stack)#최하단 원소부터 출력



#--------------------------------------------------------------------

# 큐 : 먼저 들어 온 데이터가 먼저 나가는 형식(선입선출)의 자료구조
# 큐는 입구가 출구가 모두 뚫려 있는 터널과 같은 형태로 시각화 할 수 있습니다.

#삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
#5237
#237
#2371
#23714
#3714

#파이썬에서 큐(자료구조)를 기능적으로 리스트(자료형)로 구현할 수 있지만 시간복잡도가 더 높음으로 비효율적일 수 있음으로 deque라이브러리를 사용하도록 한다.

# from collections import deque

# queue = deque()

# queue.append(5)
# queue.append(2)
# queue.append(3)
# queue.append(7)
# queue.popleft()
# queue.append(1)
# queue.append(4)
# queue.popleft()

# print(queue)
# queue.reverse()
# print(queue)

#--------------------------------------------------------------------

#재귀함수
#자기 자신을 다시 호출하는 함수

#'재귀함수를 호출합니다.'라는 문자열을 무한히 출력합니다.
#어느 정도 출력하다가 최대 재귀 깊이 초과 메세지가 출력되고 종료
# def recursive_function():
#   print('재귀 함수를 호출합니다.')
#   recursive_function()

# recursive_function()


#재귀 함수를 문제 풀이에서 사용할 때는 재귀 함수의 종료 조건을 반드시 명시합니다.
#종료 조건을 제대로 명시하지 않으면 함수가 무한히 호추뢸 수 있습니다.

# def recursive_function(i):
#   #100번째 호출을 했을 때 종료되도록 종료 조건 명시
#   if i == 100:
#     return
#   print(i, '번째 재귀함수에서', i+1, '번째 재귀함수를 호출합니다.')
#   recursive_function(i + 1)
#   print(i, '번째 재귀함수를 종료합니다.')

# recursive_function(1)

#팩토리얼 구현 예제
#0! = 1, 1! = 1

#반복적으로 구하는 n!
# def factorial_iterative(n):
#   result = 1
#   #1부터 n까지의 수를 차례대로 곱하기
#   for i in range(1, n + 1):
#     result *= i
#   return result

# #재귀적으로 구현한 n!
# def factorial_recursive(n):
#   if n <= 1:#n이 1이하인 경우 1을 반환
#     return 1
#   #n! = n * (n - 1)!
#   return n * factorial_recursive(n - 1)

# print ('반복적으로 구현:', factorial_iterative(5))
# print ('재귀적으로 구현:', factorial_recursive(5))



#-------------------------------------------------------------------

#최대 공약수 계산(유클리드 호제법)
#두 개의 자연수에 대한 최대공약수를 구하는 대표적인 알고리즘으로는 유클리드 호제법이 있습니다.
#유클리드 호제법
# 두 자연수 A, B에 대하여 (A > B)A를 B로 나눈 나머지를 R이라고 합시다.
# 이때 A와 B의 최대공약수는 B와 R의 최대공약수와 같습니다.

#유클리드 호제법의 아이디어를 그대로 재귀함수로 작성할 수 있습니다.

#예시 192 162의 최대공약수는 
#a = 192 b = 162
#a = 162 b = 30  <- 192 % 162
#a = 30  b = 12  <- 162 % 30
#a = 12  b = 6   <- 12와 6의 최대공약수를 구하면됨

# def gcd(a, b):
#   if a % b == 0:
#     return B
#   else :
#     return (b, a % b)

# print(gcd(192, 162))



#----------------------------------------------------------------------
#DFS
#깊이 우선 탐색이라고 부르며, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘입니다.
# DFS는 스택 자료구조(혹은 재귀함수)를 이용하며, 구체적인 동작 과정은 다음과 같습니다.

#1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 합니다.
#2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리합니다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냅니다.
#3. 더 이상 2번 과정을 수행할 수 없을 때까지 반복

# graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]#인덱스 0은 비워두고 1번 노드와 연결된건 2,3, 8

# def dfs(graph, v, visited):
#   #현재 노드를 방문 처리
#   visited[v] = True#해당 노드가 방문처리
#   print(v, end=' ')
#   #현재 노드와 연결된 다른 노드를 재귀적으로 방문
#   for i in graph[v]:
#     if not visited[i]:
#       dfs(graph, i, visited)

# #각 노드가 방문된 정보를 표현 (전부 false처리)
# visited = [False] * 9

# dfs(graph, 1, visited)


#----------------------------------------------------------------------
#bfs는 너비 우선 탐색이라고도 부르며, 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘
#bfs는 큐 자료구조를 이요하며, 주체적인 동작 과정은 다음과 같습니다
# 1. 탐색 시작 노드를 큐에 삽이바고 방문처리
# 2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문
# 3. 더 이상 2번의 과정을 수행 할 수 없을 떄까지 반복합니다.

# from collections import deque

# def bfs(graph, start, visited):
#   queue = deque([start])

#   visited[start] = True

#   while queue:
#     v = queue.popleft()
#     print(v, end = ' ')

#     for i in graph[v]:
#       if not visited[i]:
#         queue.append(i)
#         visited[i] = True

# visited = [False] * 9

# bfs(graph, 1, visited)



#------------------------------------------------------------------------
# 1. 문제

# N * M 크기의 얼음틀이 있다. 구멍이 뚫려있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다. 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다. 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오. 다음의 4 X 5 얼음 틀 예시에서는 아이스크림이 총 3개 생성된다.

# 00110
# 00011
# 11111
# 00000
# 2. 입력

# 첫 번째 줄에 얼음 틀의 새로 길이 N과 가로 길이 M이 주어진다.( 1<=N, M <= 1000)
# 두 번째 줄부터 N+1번째 줄까지 얼음 틀의 형태가 주어진다.
# 이때 구멍이 뚫여있는 부분은 0, 그렇지 않은 부분은 1이다.
# 3. 출력

# 한 번에 만들 수 있는 아이스크림 개수를 출력한다.
# 4. 풀이

# 입력 (Input)

# n, m 입력받음
# 2중 for문으로 2차원 배열 입력 받음
# 처리 (Process)

# DFS로 처리
# 상하좌우 함수호출 하되 재귀로 호출해서 스택에 쌓이게 함
# 출력 (Output

# 얼음 개수는 DFS 한 번 할 때마다 1씩 증가
# DFS 한 번할 때마다 연결되 얼음이 다 얼기 때문

# n, m = map(int, input().split())

# graph = []
# for i in range(n):
#   graph.append(list(map(int, input())))#맵의 정보를 받기

# def dfs(x, y):
#   if x <= -1 or x >= n or y<= -1 or y >= m:
#     return False
#   if graph[x][y] == 0:
#     graph[x][y] = 1
#     dfs(x-1, y)
#     dfs(x, y-1)
#     dfs(x+1, y)
#     dfs(x, y+1)
#     return True
#   return False


# result = 0
# for i in range(n):
#   for j in range(m):
#     if dfs(i, j) == True:
#       result += 1

# print(result)


#------------------------------------------------------------------------
# BFS 문제) 미로 탈출

# 문제

# 동빈이는 N * M 크기의 직사각형 미로에 갇혀 있다. 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 한다. 동빈이의 위치는 (1, 1)이고 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있다. 이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다. 미로는 반드시 탈출할 수 있는 형태로 제시된다. 이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오. 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.
# 입력 조건

# 첫째 줄에 두 정수 N, M(4<=N, M <= 200)이 주어집니다. 다음 N개의 줄에는 각각 M개의 정수(0 혹은 1)로 미로의 정보가 주어진다. 각각의 수들은 공백 없이 붙어서 입력으로 제시된다. 또한 시작 칸과 마지막 칸은 항상 1이다.
# 출력 조건

# 첫째 줄에 최소 이동 칸의 개수를 출력한다.
# 풀이

# 1. 입력 (Input)

# n, m 입력
# 미로 2차원 배열 -> 2중 for 문
# 2. 처리(Process)

# BFS로 처리
# 한 단계 갈 때마다 전 단계 +1
# 3. 출력

# 최종 값 출력
# from collection import deque

# n, m = map(int, input().split())

# graph = []
# graph.append(list(map(int, input())))

# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]

# def bfs(x, y):
#   queue = deque()
#   queue.append((x, y))

#   while queue:
#     x, y = deque.popleft()

#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#       if nx < 0 or ny < 0 or nx >= n or ny >= m:
#         return False
#       if graph[nx][ny] == 0:
#         continue
#       if graph[nx][ny] == 1:
#         graph[nx][ny] = graph[x][y] + 1
#         queue.append((nx, ny))
#   return graph[n - 1][m - 1]
        
# print(bfs(0, 0))




#-------------------------------------------------------------------------
# 문제
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

# 예제 입력 1  복사
# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 예제 출력 1  복사
# 1 2 4 3
# 1 2 3 4

# from collections import deque
# import sys
# #n = 노드개수, m = 간선개수 start = 시작노드 
# n, m, start = map(int, sys.stdin.readline().split())

# edgelist = [list([]) for _ in range(n + 1)]

# for _ in range(m):
#   n1, n2 = map(int, sys.stdin.readline().split())
#   edgelist[n1].append(n2)
#   edgelist[n2].append(n1)

# for edge in edgelist:
#   edge.sort()

# def bfs(edgelist, start, visited):
#   queue = deque([start])
#   visited[start] = False
#   while queue:
#     p = queue.popleft()
#     print (p, end = ' ')
#     for i in edgelist[p]:
#         if visited[i]:
#           queue.append(i)#1과 연관된 모든 노드를 추가
#           visited[i] = False#방문처리해버리기


# def dfs(edgelist, start, visited):
#   visited[start] = True
#   print(start, end = ' ')
#   #현재 노드와 연결된 다른 노드를 재귀적으로 방문
#   for i in edgelist[start]:
#     if not visited[i]:
#       dfs(edgelist, i, visited)

# visited = [False] * m
# dfs(edgelist, start, visited)
# print()
# bfs(edgelist, start, visited)



#---------------------------------------------------------------------------
#BFS 문제(너비 우선탐색)
# 문제
# N×M크기의 배열로 표현되는 미로가 있다.

# 1	0	1	1	1	1
# 1	0	1	0	1	0
# 1	0	1	0	1	1
# 1	1	1	0	1	1
# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

# 위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

# 입력
# 첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

# 출력
# 첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

# 예제 입력 1  복사
# 4 6
# 101111
# 101010
# 101011
# 111011
# 예제 출력 1  복사
# 15

# from collections import deque

# dx = [0, 0 ,1, -1]
# dy = [1, -1, 0, 0]

# n, m = map(int, input().split())
# a = [list(map(int, list(input()))) for _ in range(n)]
# q = deque()
# check = [[False] * m for _ in range(n)]
# dist = [[0] * m for _ in range(n)]

# q.append((0, 0))
# check[0][0] = True
# dist[0][0] = 1

# while q:
#   x, y = q.popleft()
#   for k in range(4):
#     nx, ny = x + dx[k], y + dy[k]
#     if 0 <= nx < n and 0 <= ny < m:
#       if check[nx][ny] == False and a[nx][ny] == 1:
#         q.append((nx, ny))
#         dist[nx][ny] = dist[x][y] + 1
#         checkp[nx][ny] = True

# print(dist[n - 1][m - 1])


#-----------------------------------------------------------------
# 문제
# <그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.



# 입력
# 첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

# 출력
# 첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

# 예제 입력 1  복사
# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000
# 예제 출력 1  복사
# 3
# 7
# 8
# 9

#단지 수, 단지별 아파수 오름차순 출력

# from collections import deque

# dx = [-1, 1, 0 ,0]
# dy = [0, 0, 1, -1]

# n = int(input())
# ap = [list(map(int, list(input()))) for _ in range(n)]
# visited = [[0] * m for _ in range(n)]

# def bfs(ap, visited, count, x, y):
#   queue = deque()
#   ap[x][y] = 0#지나간 자리는 0으로
#   while queue():
#     x, y = queue.pop()
#     for i in range(4):
#       nx, ny = x + dx[i], y + dy[i]
#       if 0 <= nx < n and 0 <= ny < n:
#         if ap[nx][ny] == 1:
#           count += 1
#           ap[nx][ny] == 0
#           queue.append((nx, ny))



# count = 1
# count = []
# for i in range(n):
#   for j in range(n):
#     if ap[i][j] == 1:
#       count.append(bfs(ap, visited, count, x, y))


# import sys

# n = int(input())

# def dfs(graph, count ,x, y):
#   graph[x][y] == 0

#   dx = [-1, 1, 0, 0]
#   dy = [0, 0, 1, -1]

#   for i in range(4):
#     nx = x + dx[i]
#     ny = y + dy[i]
#     if 0 <= nx < n and 0 <= ny < n:
#       if graph[nx][ny] == 1:
#         count = dfs(graph, count+1, nx, ny) 
#   return count


# graph = [list(map(int, list(input()))) for _ in range(n)]

# ans = []
# for i in range(n):
#   for j in range(n):
#     if graph[i][j] == 1:
#       ans.append(dfs(graph, 1, i, j))

# print(len(ans))
# for i in sorted(ans):
#   print(i)




#----------------------------------------------------------------
# 문제
# 철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다. 토마토는 아래의 그림과 같이 격자 모양 상자의 칸에 하나씩 넣어서 창고에 보관한다. 



# 창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다. 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다. 대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.

# 토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.

# 입력
# 첫 줄에는 상자의 크기를 나타내는 두 정수 M,N이 주어진다. M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 단, 2 ≤ M,N ≤ 1,000 이다. 둘째 줄부터는 하나의 상자에 저장된 토마토들의 정보가 주어진다. 즉, 둘째 줄부터 N개의 줄에는 상자에 담긴 토마토의 정보가 주어진다. 하나의 줄에는 상자 가로줄에 들어있는 토마토의 상태가 M개의 정수로 주어진다. 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.

# 토마토가 하나 이상 있는 경우만 입력으로 주어진다.

# 출력
# 여러분은 토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다. 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.

# 예제 입력 1  복사
# 6 4
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 1
# 예제 출력 1  복사
# 8

# 예제 입력 2  복사
# 6 4
# 0 -1 0 0 0 0
# -1 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 1
# 예제 출력 2  복사
# -1
# 예제 입력 3  복사
# 6 4
# 1 -1 0 0 0 0
# 0 -1 0 0 0 0
# 0 0 0 0 -1 0
# 0 0 0 0 -1 1
# 예제 출력 3  복사
# 6
# 예제 입력 4  복사
# 5 5
# -1 1 0 0 0
# 0 -1 -1 -1 0
# 0 -1 -1 -1 0
# 0 -1 -1 -1 0
# 0 0 0 0 0
# 예제 출력 4  복사
# 14

# from collections import deque

# M, N = map(int, input().split())
# tots = [list(map(int, input().split())) for _ in range(N)]
# queue = deque() # 꼭 deque를 쓰지 않아도 됨

# for i in range(N):
#     for j in range(M):
#         if tots[i][j] == 1:
#             queue.append([i, j])

# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]

# # 여기부터 bfs
# while queue:
#     row, col = queue.popleft()
    
#     for k in range(4):
#         _row = row + dy[k]
#         _col = col + dx[k]
        
#         # 안익은게 있다면, 익은 것으로 바꿔준다.
#         if 0 <= _row < N and 0 <= _col < M and tots[_row][_col] == 0:
#             tots[_row][_col] = tots[row][col] + 1
#             queue.append([_row, _col])
# # bfs 끝------

# # -1이 존재해서 -2 값으로 비교
# result = -2
# # 안익은게 있는지 체크
# check_tot = False#0

# for i in tots:
#     for j in i:
#         if(j == 0):
#             check_tot = True#1
#         result = max(result, j)#제일 큰 값을 반환
        
# if check_tot:#아직도 0이면 
#     print(-1)#-1 출력
# elif result == -1:
#     print(0)
# else:
#     print(result - 1)


#---------------------------------------------------------------------------
# 문제
# 신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.

# 예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자. 1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다. 하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.

# 어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다. 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

# 출력
# 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.

# 예제 입력 1  복사
# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7
# 예제 출력 1  복사

from collections import deque

computer = int(input())
network = int(input())
virus_map = [[0 for _ in range(computer + 1)] for _ in range(computer + 1)]

for _ in range(network):
  x, y = map(int, input().split())
  virus_map[x][y] = 1
  virus_map[y][x] = 1

def bfs(virus_map, start):
  queue = deque([start])
  visited = []

  while queue:
    temp = queue.popleft()
    visited.append(temp)

    for i in range(len(virus_map)):
      if virus_map[temp][i] and i not in visited and i not in queue:
        queue.append(i)
  return len(visited) - 1

print(bfs(virus_map, 1))
