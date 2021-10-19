
def squirrel(N):
    for i in range(1,N):
        factorial = N * (N-1)
    if factorial > 10 :
        result = factorial % 10
    else: 
        result = factorial % 1
    return result

print(squirrel(50))