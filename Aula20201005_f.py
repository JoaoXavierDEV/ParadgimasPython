# RECURSIVIDADE - FATORIAL
# 5! = 5 * 4 * 3 * 2 * 1 = 5 * 4!
# 4! = 4 * 3 * 2 * 1 = 4 * 3!

def fatorial(x):
    if x > 1 : 
        return x * fatorial(x-1)
    else:
        return 1

print(fatorial(5))
print(fatorial(3))

def fibonacci(x):
    if x==1 or x==2:
        return 1
    else:
        return fibonacci(x-1)+fibonacci(x-2)

print(fibonacci(4))

