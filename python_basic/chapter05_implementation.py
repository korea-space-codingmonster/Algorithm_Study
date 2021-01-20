#상하좌우 문제
#시뮬레이션 문제

#시뮬레이션 유형, 구현유형, 완전 탐색 유형

#N 입력 받기
#  n = int(input())
#  x , y = 1, 1
#  plans = input().split()

# # L, R, U, D에 따른 이동 방향
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move_types = ['L', 'R', 'U', 'D']

# #이동 계획을 하나씩 확인하기
# for plan in plans:
#   #이동 후 좌표 구하기
#   for i in range(len(move_types)):
#     nx = x + dx[i]
#     ny = y + dy[i]
#   #공간을 벗어난 경우 무시
#   if nx < 1 or ny < 1 or nx > n or ny > n:
#     continue
#   #이동 수행
#   x, y = nx, ny
# print(x, y)

#----------------------------------------------------

#시각 : 문제
#정수 n이 입력되면 00시 00분 00초부터 n시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포하되는 모든 경우의 수를 구하는 프로그램을 작성하세요. 예를 들어 1을 입력 했을때 다음은 3이 하나라도 포함되어 있으므로 세어야 하는 시각입니다.
#00시 00분 03초
#00시 13분 30초

#반면에 다음은 3이 하나도 포함되어 있지 않으므로 세면 안되는 시각 입니다.
#00시 02분 55초
#01시 27분 45초

#입력조건 첫째 줄에 정수 N이 입력(0 <= n <= 23)
#완전 탐색
# n = int(input())
# count = 0

# for i in range(n + 1):
#   for j in range(60):
#     for k in range(60):
#       if '3' in str(i) + str(j) + str(k):
#         count += 1
# print(count)



#----------------------------------------------------
#행복 왕국의 왕실 정원은 체스판과 같은 8x8 좌표 평면 입니다. 왕실 정원의 특정한 한 칸에 나이트가 서 있습니다. 나이트는 매우 충성스러운 신하로서 매일 무술을 연마합니다.

#나이트는 말을 타고 있기 때문에 이동을 할 떄는 L자 형태로만 이동할 수 있으며 정원 밖으로는 나갈 수 없습니다.

#나이트는 특정 위치에서 다음과 같은 2가지 경우로 이동할 수 있습니다.
#1. 수평으로 두 칸 이동항 뒤에 수직으로 한칸 이동하기
#2. 수직으로 두 칸 이동한 뒤에 수평으로 한칸 이동하기

#8x8 좌표평면에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하세요. 왕실의 정원에서 행 위치를 표현 할떄는 1부터 8로 표현하며, 열 위치를 표현할 때는 a부터 h로 표현합니다.

#a1에 있을 때 이동할 수 있는 경우의 수는 2가지 입니다.

# input_position = input()
# row = int(input_position[1])
# col = int(ord(input_position[0])) - int(ord('a')) + 1

# steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# reuslt = 0
# for step in steps:
#   next_row = row + step[0]
#   next_col = col + step[1]

# if next_col >= 1 and next_col <= 8 and next_row >= 1 and next_row <= 8:
#   result += 1

# print(result)



#----------------------------------------------------

#문자열 재정렬 : 문제 설명
#알파벳 대문자와 숫자(0 ~ 9)로만 구성된 문자열이 입력으로 주어집니다. 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.
#예를 들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력합니다.

<<<<<<< HEAD
# string = input()
# alpha = []
# value = 0

# for i in string :
#   if i.isalpha():
#     alpha.append(i)
#   else:
#     value += int(i)

# alpha.sort()

# if value != 0:
#   alpha.append(str(value))

# print(''.join(alpha))#문자열로 출력하기 위함





#----------------------------------------------------
# 현민이는 게임캐릭터가 맵 안에서 움직이는 시스템을 개발중이다. 캐릭터가 있는 장소는 1 * 1 크기의 정사각형으로 이뤄진 N * M 크기의 직사각형으로, 각각의 칸은 육지 또는 바다이다. 
# 캐릭터는 동서남북 중 한 곳을 바라본다. 

# 맵의 각칸은 (A, B)로 나타낼 수 있고, A는 북쪽으로부터 떨어진 칸의 갯수, B는 서쪽으로부터 
# 떨어진 칸의 개수이다. 캐릭터는 상하좌우로 움직일 수 있고, 바다로 되어 있는 공간에는 갈 수 없다. 캐릭터의 움직임을 설정하기 위해 정해놓은 매뉴얼은 이러하다. 

# 1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향)부터 차례대로 갈 곳을 정한다. 

# 2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진 한다. 왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다. 

# 3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어있는 칸인 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다. 단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다. 

# 현민이는 위과정을 반복적으로 수행하면서 캐릭터의 움직임에 이상이 있는지 테스트 하려고 한다. 
# 매뉴얼에 따라 캐릭터를 이동시킨 뒤에, 캐릭터가 방문한 칸의 수를 출력하는 프로그램을 만드시오. 

# 입력조건 
# - 첫째 줄에 맵의 세로 크기 N과 가로 크기 M을 공백으로 구분하여 입력한다. (N >= 3. M <= 50)  
# - 둘째 줄에 게임 캐릭터가 있는 칸의 좌표(A, B)와 바라보는 방향 d가 각각 서로 공백으로 구분하여 주어진다. 방향 d의 값은 다음과 같다. 
# - 0: 북쪽 
# - 1: 동쪽 
# - 2: 남쪽 
# - 3: 서쪽 

# 셋째 줄부터는 맵이 육지인지 바다인지 입력한다. N개의 줄에 맵의 상태가 북쪽부터 남쪽 순서대로, 각 줄의 데이터는 서쪽부터 동쪽 순서대로 주어진다. 맵의 외곽은 항상 바다로 되어있다. 
# - 0: 육지 
# - 1: 바다 

# - 처음에 게임 캐릭터가 위치한 칸의 상태는 항상 육지이다. 

# 출력조건 
# - 첫째 줄에 이동을 마친 후 캐릭터가 방문한 칸의 수를 출력한다. 


# 입력예시 

# 4 4 
# 1 1 0 
# 1 1 1 1 
# 1 0 0 1 
# 1 1 0 1 
# 1 1 1 1 

# 출력예시  
# 3

n, m = map(int, input().split())#공백구분 map의 크기 입력받기
x, y, direction = map(int, input().split())#현재 위치, 방향 받기
d = [[0] * m for _ in range(n)]#map을 전부 0처리
d[x][y] = 1#현재 위치는 1처리

array = []
for i in range(n):
  array.append(list(map(int, input().split())))#저체 맴의 정보 받기

#상 하 좌 우
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#0,1,2,3 북동남서 입력을 받으면
def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3

count = 1
turn_time = 0
#무한루프 안에서 왼쪽으로 선회하면서
while True:
  turn_left()
  nx = x + dx[direction]
  ny = y + dx[direction]
  #아직 가지 않은 곳이거나, 육지인경우
  if d[nx][ny] == 0 and array[nx][ny] == 0:
     d[nx][ny] = 1
     x = nx
     y = ny
     count += 1
     turn_time = 0
     continue
  else:
    turn_time += 1

  if turn_time == 4:
    nx = x - dx[direction]
    ny = y - dy[direction]

    if array[nx][ny] == 0:
      x = nx
      y = ny
    else:
      break
    turn_time = 0
print(count)


=======
string = input()
alpha = []
value = 0

for i in string :
  if i.isalpha():
    alpha.append(i)
  else:
    value += int(i)

alpha.sort()

if value != 0:
  alpha.append(str(value))

print(''.join(alpha))#문자열로 출력하기 위함
>>>>>>> 650f2189f87442400fd7e1e9886dc66ff889e6d6
