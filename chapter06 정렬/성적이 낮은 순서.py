# N명의 학생저옵다 있다. 학생벙보는 학생의 이름과 학생의 성적으로 구분된다. 각 학생의 이름과 성적 정보가 주어졌을때 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하여라.

# 입력예시 
# 2
# 홍길동 95
# 이순신 77

# 출력예시
# 이순진
# 홍길동

n = int(input())

array = []
for i in range(n):
  input_data = input().split()

  array.append((input().data[0], input().data[1])

array = sorted(array, key = lamda student:student[1])

for student in array:
  print(studet[0], end = ' ')
