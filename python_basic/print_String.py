#문자열 = " ", ' ' 둘다 사용 가능

# 전체 문자열을 큰 따옴표로 구성하는 경우, 내부적으로 작은 따옴표를 포함 할 수 있다.
#전체 문자열을 작은따옴표로 구성하는 경우, 내부적으로 큰따옴표를 포함할 수 있다.
#혹은 백슬레시(\)를 사용하면, 큰따옴표나 작음따옴표를 원하는 만큼 포함시킬 수 있다.

data = "Hello world"
print(data)

data = "Don't you know \"python\"?"
print(data)


#문자열 연산 변수에 (+)을 이용, 문자열이 더해져 연결
a = "Hello"
b = "World"
print(a +" "+b)

a = "string"
print(a * 3)

a = "ABCDEF"
print(a[2 : 4])

#a[2] = 'a'#불가능
