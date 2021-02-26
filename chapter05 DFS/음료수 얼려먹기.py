# DFS 문제) 음료수 얼려먹기
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

n, m = map(int, input().split())

graph = []
for i in range(n):
  graph.append(list(map(int, input())))
#graph = [list(map(int, input().split())) for _ in range(n)]

def dfs(x, y):
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return false
  
  if graph[x][y] == 0:
    graph[x][y] = 1

    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x + 1, y)
    dfs(x, y + 1)
    return True
  return  False


result = 0
for i in range(n):
  for j in range(m):
    if dfs(n, m) == True:
      result += 1

print(result)
