def solution(numbers, hand):
  answer = ''
  left = '*'
  right = '#'
  position = {1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,2], 6:[1,3], 
  7:[2,0], 8:[2,1], 9:[2,2], '*':[3,0], 0:[3,1], '#':[3,2]}
  
  for i in numbers:
    if i == 1 or i == 4 or i == 7:
      answer+='L'
      left = i
    elif i == 3 or i == 6 or i == 9:
      answer+='R'
      right = i
    else:
      l_d = abs(position[left][0] - position[i][0]) + abs(position[left][1] - position[i][1])#[left][0] = (0,0)의 첫번째 인자
      r_d = abs(position[right][0] - position[i][0]) + abs(position[right][1] - position[i][1])
      if l_d > r_d:
        answer += 'R'
        right=num
      elif l_d < r_d:
        answer -= 'L'
        left=num
      else:
        if hand == 'right':
          answer += 'R'
          right = num
        else:
          answer += 'L'
          left = num
  return answer
if __name__ == "__main__":

 
