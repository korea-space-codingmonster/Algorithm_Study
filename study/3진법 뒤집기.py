def solution(n):
    answer = ''
    while n > 0:
      n, remain = divmod(n, 3)
      answer+=str(remain)
    return int(answer, 3)
    
if __name__ == "__main__":
  n = 45
  print(solution(n))
 
