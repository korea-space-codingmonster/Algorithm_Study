#표준 입출력 함수

#input() 함수는 한 줄의 문자열을 입력 받는 함수
#map() 함수는 리스트의 모든 원소에 각각 특정한 함수를 적용할 떄 사용


#n = int(input())#정수로 입력
#data = input()
#print(n)
#print(data)


#공백을 기준으로 구분된 데이터를 입력 받을 떄는 다음과 같이 사용
  #에시 list(map(int, input().split()))
  #예시 공백을 기준으로 구분된 데이터의 개수가 많지 않다면, 단순히 다음과 같이 사용
  #a,b,c = map(int, input().split())
#n = int(input())
#data = list(map(int, input().split()))

#print(n)
#print(data)

#a ,b, c = map(int, input().split())
#print(a,b,c)



#사용자로부터 입력을 최대한 빠르게 받아야 하는 경우가 있습니다
# 파이썬의 경우 sys라이브러리에 정의되어 있는 sys.stdin.readline()메서드를 이용합니다
  #단, 입력 후 엔터(enter)가 줄 바꿈 기호로 입력되므로 rstrip() 메서드를 함께 사용합니다.
#import sys

#문자열
#data = sys.stdin.readline().rstrip()
#print(data)




#표준출력은 print() 함수를 이용합니다.
  #각 변수를 콤마(,)를 이용하여 띄어쓰기로 구분하여 출력할 수 있습니다.
#print()는 기본적으로 출력 이후에 줄 바꿈을 수행합니다.
  #줄 바꿈을 원치 않는 경우 'end' 속성을 이용할 수 있습니다.
#에씨
a = 1
b = 2
print(a, b)
print(7, end = " ")
print(8, end = " ")

#출력할 변수
answer = 7
print("정답은" + str(answer) + "입니다.")



#---------------------------------------------------------------------
#f-string
#파이썬 3.6부터 사용 가능하며 문자열 앞에 접두산 'f'를 붙여 사용합니다.
#중괄호 안에 변수명을 기입하여 문자열과 정수를 함께 넣을 수 있습니다.

answer = 7
print(f"정답은 {answer}입니다.")