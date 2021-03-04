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