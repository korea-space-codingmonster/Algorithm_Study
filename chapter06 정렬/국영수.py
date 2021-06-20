N = int(input())

array = []
for i in range(N):
  input_data = input().split()
  array.append((input_data[0], int(input_data[1]), int(input_data[2], int(input_data[3]))))

sorted_score_list = sorted(array, key = lambda x : (-x[1], x[2], -x[3], [0]))

for i in sorted_score_list:
  print(array[0])

