##0+1+1+2+3+5+8+13+21.....

def fib(num):
   if num <= 0:
       return 0
   elif num == 1:
       return 1
   else:
       return fib(num-1)+fib(num-2)
   
n = int(input("Kis number tak ka fibonacci?"))
print(f"Fibonacci of {n} is:", fib(n))
