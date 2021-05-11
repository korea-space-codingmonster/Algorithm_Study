# 이진 탐색 문제) 부품 찾기

# 1. 문제

# 동빈이네 전자 매장에는 부품이 N개 있다. 각 부품은 정수 형태의 고유한 번호가 있다. 어느 날 손님이 M개의 종류의 부품을 대량으로 구매하겠다며 당일 날 견적서를 요청했다. 동빈이는 때를 놓치지 않고 손님이 문의한 부품 M개 종류를 모두 확인해서 견적서를 작성해야 한다. 이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성해보자.
# 예를 들어 가게의 부품이 총 5개일 때 부품 번호가 다음과 같다고 하자.

# N=5
# [8, 3, 7, 9, 2]
# 손님은 총 3개의 부품이 있는지 확인 요청했는데 부품 번호는 다음과 같다.

# M=3
# [5, 7, 9]
# 이때 손님이 요청한 부품 번호의 순서대로 부품을 확인해 부품이 있으면 yes를, 없으면 no를 출력한다. 구분은 공백으로 한다.

# 2. 입력

# 첫째 줄에 정수 N이 주어진다. (1<=N<=1,000,000)
# 둘째 줄에는 공백으로 구분하여 N개의 정수가 주어진다. 이때 정수는 1보다 크고 1,000,000 이하이다.
# 셋째 줄에는 정수 M이 주어진다. (1<=M<=100,000)
# 넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다. 이때 정수는 1보다 크고 10억 이하이다.
# 3. 출력

# 첫째 줄에 공백으로 구분하여 각 부품이 존재하면 yes를, 없으면 no를 출력한다.

# 입력예시
# 5
# 8 3 7 9 2
# 3
# 5 7 9

#출력예시
#no yes yes




# ------------------------------------------------------------

# <코딩테스트를 위한 내용>
 
# Python에서 입력값을 받을 때 input() 함수를 사용하지만 시간단축을 위해 sys.stdin.readline을 사용한다.
 
# 입출력 속도 비교 : sys.stdin.readline > raw_input() > input()
 
# 변형 : 
# num = int(input())   ->  num = int(sys.stdin.readline())
# 사용 시, import sys  선언 필요
 
 
# 여러 라인 입력 받을 경우 아래와 같이 사용하는 게 빠르다고 함.
# n = input()
# a = [sys.stdin.readline() for i in range(n)]


 
# sys.stdin.readline : 
# 한 라인 입력 받을 떄
 
# sys.stdin : 
# 여러 줄 입력 받을 때
# for line in sys.stdin: 
#     print(line)
 
 
 
# * 재귀함수가 있는 경우 재귀 깊이를 설정해야 한다. (python3 의 경우 사용가능 / pypy에서는 사용 불가)
 
# sys.setrecursionlimit(10**8) # 10^8 까지 늘림.

 
 
 
# * pypy : python 구동을 더 빠르게 시켜준다. (개선된 python)

# ------------------------------------------------------------


# 이진탐색을 이용한 방법

# def  binary_search(array, target, start, end):
   
#   while start <= end:
#     mid = (start + end) // 2

#     if array[mid] == target:
#       return mid
#     elif array[mid] > target:
#       end = mid - 1
#     else:
#       start = mid + 1
#   return None

# n = int(input())
# array = list(map(int, input().split()))
# array.sort()

# m = int(input())
# x = list(map(int, input().split()))

# for i in x:
#   result = binary_search(array, i, 0, n-1);
#   if result != None:
#     print('yes', end = ' ')
#   else:
#     print('no', end = ' ')
 

# ------------------------------------------------------------
#계수정렬을 이용

# n = int(input())
# array = [0] * 1000001
# for i in input().split():
#   array[int(i)] = 1

# m = int(input())
# x = list(map(int, input().split()))

# for i in x:
#   if array[i] == 1:
#     print('yes', end = ' ')
#   else:
#     print('no', end = ' ')



# ------------------------------------------------------------


