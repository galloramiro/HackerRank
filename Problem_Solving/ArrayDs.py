def reverseArray(a):
    return [a[i]for i in range(len(a)-1,-1,-1)]
    #narr = []
    #for i in range(len(a)-1,-1,-1):
    #    narr.append(a[i])
    #print(narr)



print(reverseArray([1,4,3,2]))             # 2 3 4 1