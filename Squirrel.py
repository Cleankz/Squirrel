def squirrel(N):
    factorial = 1
    for i in range(1,N+1):
        factorial *= i
    result = factorial
    str_of_factorial = str(factorial)
    for i in range(len(str_of_factorial)-1):
        result = result // 10
    return result