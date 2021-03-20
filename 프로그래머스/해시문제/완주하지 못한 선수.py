# 동명이인도 생각을 해야한다.
# pa = int(input())

# participant = {}
# completion = {}
# for i in range(pa):
#   participant[i] = input()
  
# for i in range(pa - 1):
#   completion[i] = input()

# dic = {}
# def solution(participant, completion):
#   for i in participant:
#     if i not in participant:
#       dic[i] = 1
#     else:
#       dic[i] += 1
  
#   for j in completion:
#     if j not in completion:
#       dic[j] -= 1
    
#   for k in dic.keys():
#     if dic[k] != 0:
#       answer = k
#       break
#   return answer

#--------------------------------------------------
    
# 'collections'를 이용해보자!

# - import collections
# - collections에 내장된 함수인 Counter()는 Dic과 같이 hash형 자료들의 값의 개수를 셀 때 사용
# - Dic처럼 {Key:value}형식으로 만들어짐
# - Counter()객체 끼리 뺴는 것도 가능
# - 0(zero)나 음수(minus)의 값들고 가능
# - 해당하는 값이 없더라도 error가 아닌 0을 반환


import collections
lst = ['aa', 'cc', 'dd', 'aa', 'bb', 'ee']
print(collections.Counter(lst))

def solution(p. c):
  p.sort()
  c.sort()
  result = collections.Counter(p) - collections.Counter(c)
  return list(result)[0]