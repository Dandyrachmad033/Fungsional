# NIM Ganjil
def fib(n):
    
    a,b=0,1
    for i in range(n):
        yield a
        a, b = b, a+b
a = fib(int(input("Masukkan Jumlah Deret Fibonacci: ")))
while True:
    
    try:print(next(a))
    except StopIteration:
        break


