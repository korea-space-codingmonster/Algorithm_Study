
def main(n, arr1, arr2):
    answer = []
    arr1_list = []
    arr2_list = []
    result = []
    for i in range(0, n):
        arr1_list.append(bin(arr1[i]))
        arr2_list.append(bin(arr2[i]))
        a = str(int(arr1_list[i] + arr2_list[i]))
        if len(a) < n:
          a = '0'*(n -len(a)) + a
        for j in a:
          

    print(a)
    
if __name__ == "__main__":
  n = 5
  arr1 = [9, 20, 28, 18, 11]
  arr2 = [30, 1, 21, 17, 28] # i = 2, j = 5, k = 3
  main(4, arr1, arr2)