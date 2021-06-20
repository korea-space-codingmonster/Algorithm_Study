def heapify(list, inex, n):
  l = index * 2#left
  r = index * 2 + 1#right
  s_index = index#작은 인덱스
  if (l <= n)

def heap_sort(v):
  n = len(v)
  v = [0] + v

  #min heap 생성
  for i in range(n, 0, -1):# n ~ 0까지 -1 간격으로
    heapify(v, i, n)#list, index, 개수
