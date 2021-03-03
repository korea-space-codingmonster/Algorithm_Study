#기본 선택정렬의 이해

#반복문을 돌면서 가장 작은 것이 나오면 맨 앞의 수와 하나씩 바꾼다.
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
  min_index = i
  for j in range(i + 1, len(array)):
    if array[min_index] > array[j]:
      min_index = j
  array[i], array[min_index] = array[min_index], array[i]

print(array)
