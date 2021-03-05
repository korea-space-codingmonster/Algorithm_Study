# 하나의 주열에는 다양한 수가 존재한다. 이러한 수의 크기에 상관없이 나열되어 있다.
# 이 수를 큰 수부터 작은 수의 순서로 정렬해야한다. 수열을 내림차순으로 정렬하는 프로그램을 만드시오.

# 입력조건
# 첫째 줄에 수열에 속해 있는 수의 개수 N이 주어진다.(1 < N <= 500)
# 둘째 줄부터 N + 1번째 줄까지 N개의 수가 입려된다. 수의 범위는 1이상 100000이하의 자연수이다.

# 입력예시 
# 3
# 15
# 27
# 12

# 출력예시
# 27 15 12

n = int(input())

array = []

for i in range(n):
  array.append(int(input()))

array = sorted(array, reverse = True)

for i in array:
  print(i, end = ' ')

