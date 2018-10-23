def miniMaxSum(arr):
    sArr = sorted(arr)                                      # La guardo con sorted(arr) y no arr.sort() ya que este último no devuelve el valor para ser tomado después. 
    maxSum = sArr[1] + sArr[2] + sArr[3] + sArr[4]
    minSum = sArr[0] + sArr[1] + sArr[2] + sArr[3]

    print(minSum, maxSum)



miniMaxSum([1,3,5,9,7])         # 16 24
miniMaxSum([1,2,3,4,5])         # 10 14
