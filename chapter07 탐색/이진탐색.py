# 재귀 함수로 구현한 이진 탐색 소스코드
# def   binary_search(array, target, start, end):
#   if start > end:
#     return None
#   mid = (end + start) // 2
  
#   if array[mid] == target:#mid가 찾는 값인 경우
#     return mid;
#   elif array[mid] > target:
#     return binary_search(array, target, start, mid - 1)
#   else:
#     return binary_search(array, target, mid + 1, end)


# n, target = list(map(int, input().split()))#원소의 개수와 찾는 숫자입력
# array = list(map(int, input().split()))#전체 원소 개수
# result = binary_search(array, target, 0, n - 1)

# if result == None:
#   print("원소가 존재하지 않습니다.")
# else:
#   print(result + 1)


# 반복문으로 구현한 이진 탐색 코드
n, target = list(map(int, input().split()))
array = list(map(int, input().split()))
result = binary_search(array, target, 0, n - 1)

if result = None:
  print("원소가 존재하지 않습니다.")
else
  print(result + 1)


def   binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    #찾는 경우 중간점 인덱스 반환
    if target == array[mid]:
      return mid;
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return None
