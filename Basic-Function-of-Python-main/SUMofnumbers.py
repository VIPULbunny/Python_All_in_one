def sumofn(n):
    if n == 0 :
        return 0
    return sumofn(n-1) + n
print(sumofn(4))