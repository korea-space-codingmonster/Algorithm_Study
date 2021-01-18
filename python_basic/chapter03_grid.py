#base

# n = 1260
# count = 0

# array = [500, 100, 50, 10]

# for coin in array:
#   count +=n // coin
#   n %= coin

# print(count)



#-----------------------------------------------------------
#큰수의 법칙
# n, m, k = map(int, input().split())

# data = list(map(int, input().split()))
# data.sort()

# first = data[n - 1]
# second = data[n - 2]
# result = 0

# while True:
#   for i in range(k):
#     if m == 0:
#       break
#     result += first
#     m -= 1
#   if m == 0:
#     break
#   result += second
#   m -= 1
# print(result)


#수학적으로 생각했을 경우
# n, m, k = map(int, input().split())

# data = list(map(int, input().split()))
# data.sort()

# first = data[n - 1]
# second = data[n - 2]

# count = int(m / (k + 1)) * k
# count += m % (k + 1)

# result = 0
# result += (count) * first
# result += (m - count) * second

# print(result)


#-----------------------------------------------------------
#숫자 카드 게임
# n, m = map(int, input().split())

# result = 0

# for i in range(n):
#   data = map(int, input().split())
#   min_value = min(data)
  
#   result = max(result, min_value)
# print(result)

#숫자 카드 게임
#이중 반복문
# n, m = map(int, input().split())

# result = 0 

# for i in range(n):
#   data = map(int, input().split())

#   min = 10001
#   for j in data:
#     min_value = min(data)
#   result = max(result, min_value)

# print(result)


#-----------------------------------------------------------
#
#1이 될 때까지
# n, k = map(int, input().split())
# result = 0

# while n >= k:

#   while n % k != 0:
#     n -= 1
#     result += 1
  
#   n //= k
#   result += 1

# while n > 1:
#   n -= 1
#   result += 1

# print(result)


#-----------------------------------------------------------

# 문제
# 상근이는 요즘 설탕공장에서 설탕을 배달하고 있다. 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다. 설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.

# 상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다. 예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만, 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.

# 상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)

# 출력
# 상근이가 배달하는 봉지의 최소 개수를 출력한다. 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.


N = int(input())
count = 0

while N >=0:
  if N % 5 == 0:
    count += N // 5
    print(count)
    break
  N -= 3
  count += 1
else:
  print("-1")



  #-----------------------------------------------------------