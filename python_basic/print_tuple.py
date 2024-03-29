#튜플 사용

a = (1,2,3,4,5,6,7,8,9)

#네번째 원소만 출력
print(a[3])

print(a[1 : 4])#범위값 출력 a[1], a[2], a[3]출력

a = (1,2,3,4)
print(a)
#a[2] = 7 # 바꾸는건 불가능


#튜플을 사용하면 좋은 경우
#서로 다른 성질의 데이터를 묶어서 관리해야할때
#  최단 경로 알고리즘에서는 (비용, 노드번호)의 형태로 튜플 자료형을 자주 사용
#데이터의 나열을 해싱의 키 값으로 사용해야할 때
#  튜플은 변경이 불가능하므로 리스트와 다르게 키 값으로 사용 될 수 도 있음
#리스트보다 메모리를 효율적으로 사용해야 할때



#<사전 자료형은 키(key)와 값(value)의 쌍을 데이터로 가지는 자료형>
#사전 자료형
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Cocont'

print(data)

if '사과' in data:
  print("'사과'를 키로 가지는 데이터가 존재합니다.")

  #키 값만 뽑아낼때 key() 
  #값을 뽑아낼 때value()

#  b = {'홍길동' : 97}

  key_list = list(data.keys())
  print(key_list)





#집합 자료형
data = set([1,1,2,3,4,4,5])
print(data)

#집합 자료형 초기화 방법
data = {1,1,2,3,4,4,5}
print(data)

#합집합 교집합 차집합 연산등이 가능하다.
a = set([1,2,3,4,5,6])
b = set([3,4,5,6,7])

#합집합
print(a | b)

#교집합
print(a & b)

#차집합
print(a - b)




#집합 자료형 관련 함수
data = set([1,2,3])
print(data)

#원소 하나 추가
data.add(4)
print(data)

#원소 여러개 추가
data.update([5,6])
print(data)


#특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)


#사전 자료형과 집합 자료형의 특징
#리스트나 튜풀은 순서가 있기 떄문에 인덱싱을 통해 자료형의 값을 얻을 수 있습니다.
#사전 자료형과 집합 자료형은 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없습니다.
  #사전의 key(키 값) 혹은 집합의 원소(element)를 이용해 0(1)이 시간 복잡도로 조회합니다.