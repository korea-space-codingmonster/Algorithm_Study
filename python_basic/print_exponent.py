a = 1e9
print(a)# 1,000,000,000.0

a = 75.15e1
print(a)#7.515

a = 3954e-3
print(a)#3.954


#컴퓨터는 정확하게 0.9라는 수를 가지고 있을 수 없다.
a = 0.3 + 0.6
print(a)

if a == 0.9:
  print(True)
else :
  print(False)

  #방법은 round()함수 를 사용 -> 반올림

a = 0.3 + 0.6
print(round(a, 4))#소수점 아래 5자리에서 반올림
if round(a, 4) == 0.9:
  print(True)
else :
  print(False)



##수 자료형의 연산
a = 5
b = 3
print(a/b)
print(a ** b)
print(a ** 0.5)
