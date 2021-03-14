# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

# 예제 입력 1  복사
# 5
# 5
# 4
# 3
# 2
# 1
# 예제 출력 1  복사
# 1
# 2
# 3
# 4
# 5


#수의 개수가 1,000,000임으로 수가 많아 퀵정렬을 한번 써볼까?
#<그냥 코드>
# n = int(input())

# array = []
# for i in range(n):
#   array.append(int(input()))

# def quick_sort(array):
#   if len(array) <= 1:
#     return array

#   pivot = array[0]
#   tail = array[1:]

#   left_side = [x for x in tail if x <= pivot]
#   right_side = [x for x in tail if x > pivot]

#   return quick_sort(left_side) + [pivot] + quick_sort(right_side)

# print(quick_sort(array))
  



n = int(input())

array = []
for i in range(n):
  array.append(int(input()))

#병합 정렬(merge sort)
def merge_sort(array):
  if len(array) <= 1:
    return array
  
  mid = len(array) // 2
  left = merge_sort(array[:mid])#배열
  right = merge_sort(array[mid:])#배열

  j, i, k = 0, 0, 0

  while i < len(left) and j < len(right):
    if  left[i] < right[j]:
      array[k] = left[i]
      i += 1
    else :
      array[k] = right[j]
      j += 1
    k += 1

  if i == len(left):
    while j < len(right):
      array[k] = right[j]
      j += 1
      k += 1
  elif j == len(right):
    while i < len(left):
      array[k] = left[i]
      i += 1
      k += 1
  return array

print(merge_sort(array))

#