# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

# 예제 입력 1  복사
# 5
# 5
# 2
# 3
# 4
# 1
# 예제 출력 1  복사
# 1
# 2
# 3
# 4
# 5

# <파이썬 라이브러리를 쓴 경우>
# n = int(input())
# array = []

# for _ in range(n):
#     array.append(int(input()))

# array = sorted(array)

# for i in array:
#     print(i)



#<그냥 짠 경우>

n = int(input())

array = []
for _ in range(n):
  array.append(int(input()))

for i in range(len(array)):
  min_index = i
  for j in range(i + 1, len(array)):
    if array[min_index] > array[j]:
      min_index = j
  array[min_index], array[i] = array[i], array[min_index]

print(array)