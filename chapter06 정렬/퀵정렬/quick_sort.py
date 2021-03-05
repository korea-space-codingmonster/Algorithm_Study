array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
  if start > end:
    return
  pivot = start
  left = start + 1
  right = end
  while left <= right:#엇갈리는 경우 바꾸고 계속 진행해야함으로
    #피벗보다 큰 데이터를 찾을 때까지 반복
    while left <= end and array[left] <= array[pivot]:
      left += 1#피벗보다 작은 수를 찾는다.
    while right > start and array[right] >= array[pivot]:
      right -= 1#피벗보다 큰 수를 찾는다
    if left > right:
      array[right], array[pivot] = array[pivot], array[right]
    else:
      array[left], array[right] = array[right], array[left]
  quick_sort(array, start, right - 1)
  quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)




#파이썬으로 작성
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def   quick_sort(array):
  #리스트가 하나 이하의 원소만을 담고 있다면 종료
  if len(array) <= 1:
    return array
  
  pivot = array[0]
  tail = array[1:]

  left_side = [x for x in tail if x <= pivot]#pivot보다 작은 것들이 모여지고 자동으로 순차적으로 쌓임
  right_side = [x for x in tail if x > pivot]#pivot보다 큰 것들이 모여짐

  return quick_sort(left_side) + [pivot] + quick_sort(right_side)

  print(quick_sort(array))