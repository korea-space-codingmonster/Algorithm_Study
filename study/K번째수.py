
def main(array, commands):
    answer = []
    for i in range(commands[0]-1, commands[1]):#2,5
        answer.append(array[i])
    answer.sort()
    return answer[commands[2]-1]
    
if __name__ == "__main__":
  array = [1,5,2,6,3,7,4]
  commands = [2,5,3] # i = 2, j = 5, k = 3
  print(main(array, commands))
