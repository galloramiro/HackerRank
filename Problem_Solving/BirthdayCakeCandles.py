# https://www.hackerrank.com/challenges/birthday-cake-candles/problem

def birthdayCakeCandles(ar):
    return(ar.count(max(ar)))




print(birthdayCakeCandles([4, 4, 1, 3]))     # 2
print(birthdayCakeCandles([3, 2, 1, 3]))     # 2 