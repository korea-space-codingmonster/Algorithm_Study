#정렬 : 데이터를 특정한 기준에 따라서 순서대로 나열하는 것을 의미
#사람의 뇌는 정렬되지 않은 숫자 카드를 보고 빠르게 훑고 우리도 모르게 데이터의 규칙성을 파악하지만 컴퓨터에게는 쉽지 않은 일이다. 컴퓨터는 인간과 같이 규칙성을 직관적으로 파악할 수 없다.


#<선택정렬>
# 데이터가 무작위로 여러개 가 있을때, 이 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그 다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정을 반복한다.

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(array):
  minimum = i
  for j in range(i+1, len(array)):
    if array[minimum] > array[j]:
       minimum = j
  array[i], array[minimum] = array[minimum], array[i]

print(array)

#선택정렬의 시간복잡도는 O(N^2) for문이 두번이 있기때문에


    
      