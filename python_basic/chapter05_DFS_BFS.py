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

def recursive_function(i):
  #100번째 호출을 했을 때 종료되도록 종료 조건 명시
  if i == 100:
    return
  print(i, '번째 재귀함수에서', i+1, '번째 재귀함수를 호출합니다.')
  recursive_function(i + 1)
  print(i, '번째 재귀함수를 종료합니다.')

recursive_function(1)

#팩토리얼 구현 예제
#0! = 1, 1! = 1

#반복적으로 구하는 n!
def factorial_iterative(n):
  result = 1
  #1부터 n까지의 수를 차례대로 곱하기
  for i in range(1, n + 1):
    result *= i
  return result

#재귀적으로 구현한 n!
def factorial_recursive(n):
  if n <= 1:#n이 1이하인 경우 1을 반환
    return 1
  #n! = n * (n - 1)!
  return n * factorial_recursive(n - 1)

print ('반복적으로 구현:', factorial_iterative(5))
print ('재귀적으로 구현:', factorial_recursive(5))

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


