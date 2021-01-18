#base

# n = 1260
# count = 0

# array = [500, 100, 50, 10]

# for coin in array:
#   count +=n // coin
#   n %= coin

# print(count)


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
n, m, k = map(int, input().split())

data = list(map(int, input().split()))
data.sort()

first = data[n - 1]
second = data[n - 2]

count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)


