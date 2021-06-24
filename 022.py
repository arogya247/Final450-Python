def factorial(n):
        f = 1
        while n:
            f = f*n
            n-=1
            
        res = [int(x) for x in str(f)]
        return res
        
        
        
print(factorial(8))
