# mutable과 immutable에 대해 구분해보자.

#list는 mutable이다

# def main():
#   a = [1, 2, 3]
#   print(id(a))

#   a[0] = 5
#   print(id(a))


# if __name__ == "__main__":
#   main()
#-----------------------------------------------------------------
  #set도 mutable

# def main():
#   x = {1, 2, 3}
#   print(x)
#   print(id(x))

#   x|={4, 5, 6}
#   print(x)
#   print(id(x))

# if __name__ == "__main__":
#   main()


#-----------------------------------------------------------------
# str은 immutable 입니다.
# def main():
#   s = "abc"
#   print(s)
#   print(id(s))

#   s[0] = 's'
#   print(id(s))

# if __name__ == "__main__":
#   main()


#----------------------------------------------------------------------

#immutable한 객체의 변수간 대입
# def main():
#   a = "abc"
#   b = a
#   print(a)
#   print(b)
#   print(id(a))
#   print(id(b))

#   b = "abcd"
#   print(a)
#   print(b)
#   print(id(a))
#   print(id(b))

# if __name__ == "__main__":
#   main()

#-------------------------------------------------------------------------
#얕은 복사

# ==, is의 차이

# is 는 변수가 같은 object(객체)를 가리키면 True
# == 는 변수가 같은 Value(값)을 가지면 True

# a = [1, 2, 3]
#b = a
#c = [1, 2, 3]
#a is b
# True
#a is c
# False

# def main():
#   a = [1, 2, 3]
#   b = a[:]#a값 전부 복사
#   print(a)
#   print(b)
#   print(id(a))
#   print(id(b))

#   if a == b:
#     print("True")
#   else:
#     print("False")

#   if a is b:
#     print("True")
#   else:
#     print("False")
# # 새로운 주소 아이디가 부여되는 것을 알 수 있음
# if __name__ == "__main__":
#   main()


# ------------------------------------------------------------------
#리스트 안에 값은 리스트 자체는 다른 주소를 가지지만, 리스안의 값은 같은 주소 값을 가지고 있다.
# def main():
#   a = [[1,2], [3,4]]
#   b = a[:]

#   print(id(a))
#   print(id(b))

#   print(id(a[0]))
#   print(id(b[0]))

# if __name__ == "__main__":
#   main()

#---------------------------------------------------------------------
# 그렇다면 a[1]의 값을 바꿔보면, a[1]의 값도 바뀌지만 b[1]값도 따라 변경된다.(같은 주소를 가지고 있기 떄문)


# def main():
#   a = [[1,2], [3,4]]
#   b = a[:]

#   print(id(a))
#   print(id(b))

#   print(id(a[0]))
#   print(id(b[0]))

#   a[1].append(5)
#   print(a)
#   print(id(a[1]))

#   print(b)
#   print(id(b[1]))

# if __name__ == "__main__":
#   main()

#-----------------------------------------------------------------------------
# copy 메소드또한 얕은 복사입니다.
# import copy

# def main():
#   a = [[1, 2], [3, 4]]
#   b = copy.copy(a)

#   a[1].append(5)
#   print(a)
#   print(id(a))
#   print(b)
#   print(id(b))

# if __name__ == "__main__":
#   main()

#-----------------------------------------------------------------------------

#깊은 복사는 내부에 객체들까지 모두 새롭게 copy되는 것을 의미합니다.

import copy
a = [[1,2], [3,4]]

b = copy.deepcopy(a)
a[1].append(5)

print(a)

print(b)