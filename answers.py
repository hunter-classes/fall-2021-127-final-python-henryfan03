def isIncreasing(L):
  """
  takes a list as a parameter, indexes through the list looking for any occurance where L[i+1] <= L[i], and returns False if that condition is fulfilled, otherwise returns False.
  """
  for i in range(len(L)-1):
    if L[i+1] <= L[i]:
      return False
  return True

def numConvert(nums):
  """
  takes a list of single digit integers as a parameter, iterates through the list and concactonates the character version of the numbers in the list to a resulting variable, and returns the final concactonated string as an integer.
  """
  result = ""
  for num in nums:
    result = result + str(num)
  return int(result)

def BinConvert(binstring):
  """
  takes a binary value in the form of a string as a parameter, declares the maximum exponent of the binary digits using the length of the string, declares a reversed list starting from the max exponent to 0, then iterates through the binary string, where when a digit in the string == 1, the resulting variable will be equal to itself + 2(base value of binary) raised to the power of the exponent varialbe.
  """
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
  print("isIncreasing([1,2,7]):",isIncreasing([1,2,7]),"Expected: True")
  print("\n----------------------------------------\n")
  print("Running tests for numConvert:\n")
  print("numConvert([1,2,3]):",numConvert([1,2,3]),"Expected:",123)
  print("numConvert([0,0,7]):",numConvert([0,0,7]),"Expected:",7)
  print("numConvert([0,2,0]):",numConvert([0,2,0]),"Expected:",20)
  print("numConvert([1,0,0]):",numConvert([1,0,0]),"Expected:",100)
  print("numConvert([1,2,7]):",numConvert([1,2,7]),"Expected:",127)
  print("\n----------------------------------------\n")
  print("Running tests for BinConvert:\n")
  print("BinConvert('1'):",BinConvert('1'),"Expected:",1)
  print("BinConvert('10'):",BinConvert('10'),"Expected:",2)
  print("BinConvert('11'):",BinConvert('11'),"Expected:",3)
  print("BinConvert('100'):",BinConvert('100'),"Expected:",4)
  print("BinConvert('101'):",BinConvert('101'),"Expected:",5)
  print("BinConvert('1011'):",BinConvert('1011'),"Expected:",11)
  print("BinConvert('1111111'):",BinConvert('1111111'),"Expected:",127)

def main():
  tests()

if __name__ == "__main__":
  main()