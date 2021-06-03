
absolutes = [4,7,12]
signs = [True,False,True]
def main(absolutes, signs):
  list = []
  for i in range(0, len(absolutes)):
      if signs[i] == True:
          list.append(absolute[i])
      elif signs[i] == False:
          list.append(-1 * absolute[i])
  return sum(list)


if __name__ == "__main__":
  main(absolutes, signs)
