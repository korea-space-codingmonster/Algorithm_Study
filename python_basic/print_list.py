# 데이터를 연속적으로 담아 처리하기 위해 사용하는 자료형

# 사용자 입장에서 c나 자바에서의 배열(array)의 기능 및 연결 리스트와 유사한 기능을 지원)
# c++ 에서의 STL vector와 기능적으로 유사
# 리스트 대신에 배열 혹은 테이블이라고 부르기도 합니다.


a = [1,2,3,4,5,6,7,8,9]
print(a)

a[5] = 9
print(a)
print(a[3])#네번째 접근
print(a[8])#9번째



n = 10
a = [0] * n
print(a)

n = 20
a = [1] * n
print(a)


#인덱싱
a = [1,2,3,4,5,6,7,8,9]
print(a[7])#여덞번쨰만 출력
print(a[-1])#뒤에서 첫 번째 원소만 출력
print(a[-3])#뒤에서 세번쨰 원소 출력
a[3] = 7#네번쨰 원소 값 변경
print(a)
print("\n")


#슬라이싱
a = [1,2,3,4,5,6,7,8,9]
print(a[3])
print(a[1:4])#두 번쨰 원소부터 네번쨰 원소까지

#리스트 컴프리헨션
array = [i for i in range(10)]#(for i in range(10) = i라는 값이 10까지 반복)
print(array)

array = [i for i in range(20) if i % 2 == 1]#i % 2 == 1(wmr, 홀수만 포함하는 i만)
print(array)
array = [i * i for i in range(1, 10)]#1부터 9까지 i*i만 출력
print(array)

#리스트 컴프리헨션을 이용한 2차원 리스트
n = 4
m = 3
array = [[0] *m for _ in range(n)]#n번(세로) 반복할때마다 가로길이 m이 반복
print(array) 


#리스트 관련 기타 메서드
a = [1,4,3]
print("기본리스트:",a)

a.append(2)
print("삽입 :" ,a)

a.sort()
print("오름차순 정렬:", a)

a.sort(reverse = True)
print("내림차순 정렬:", a)


a = [4,3,2,1]
a.reverse()
print("원소 뒤집기 :",a)

a.insert(2,3)
print("인덱스 2에 3 추가:", a)

print("값이 3인 데이터 개수:", a.count(3))

a.remove(1)
print("값이 1인 데이터 삭제:", a)


a = [1,2,3,4,5,5,5,5,5]
remove_set = {3, 5}

result = [i for i in a if i not in remove_set]#remove_list에 포함되지 않는 값만을 저장
print(result)