def isIncreasing(L):
  for i in range(len(L)-1):
    if L[i+1] <= L[i]:
      return False
  return True

def numConvert(nums):
  result = ""
  for num in nums:
    result = result + str(num)
  return int(result)

def BinConvert(binstring):
  result = 0
  maxexponent = len(binstring)-1
  #inversed array of indexes to align with exponents of corresponding binary digits.
  exponents = list(range(maxexponent,-1,-1))
  for i in range(len(binstring)):
    if binstring[i] == "1":
      result = result + (2 ** exponents[i])
  return result

def tests():
  print("Running tests for isIncreasing:\n")
  print("isIncreasing([1,2,3]):",isIncreasing([1,2,3]),"Expected: True")
  print("isIncreasing([-10,0,5]):",isIncreasing([-10,0,5]),"Expected: True")
  print("isIncreasing([999,1000,-100]):",isIncreasing([999,1000,-100]),"Expected: False")
  print("isIncreasing([5,5,5]):",isIncreasing([5,5,5]),"Expected: False")
  print("isIncreasing([9,8,7]):",isIncreasing([9,8,7]),"Expected: False")
  print("\n----------------------------------------\n")
  print("Running tests for numConvert:\n")
  print("numConvert([1,2,3]):",numConvert([1,2,3]),"Expected:",123)
  print("numConvert([0,0,5]):",numConvert([0,0,5]),"Expected:",5)
  print("numConvert([0,1,0]):",numConvert([0,1,0]),"Expected:",10)
  print("numConvert([6,0,0]):",numConvert([6,0,0]),"Expected:",600)
  print("numConvert([6,1,5]):",numConvert([6,1,5]),"Expected:",615)
  print("\n----------------------------------------\n")
  print("Running tests for BinConvert:\n")
  print("BinConvert('1'):",BinConvert('1'),"Expected:",1)
  print("BinConvert('10'):",BinConvert('10'),"Expected:",2)
  print("BinConvert('11'):",BinConvert('11'),"Expected:",3)
  print("BinConvert('100'):",BinConvert('100'),"Expected:",4)
  print("BinConvert('101'):",BinConvert('101'),"Expected:",5)
  print("BinConvert('1011'):",BinConvert('1011'),"Expected:",11)

def main():
  tests()

if __name__ == "__main__":
  main()