# Time: O(n)
# Space: O(n)

def productExceptSelf(arr, n):
    prod = [1]*n
    temp = 1
    for i in range(n):
        prod[i] = temp
        temp*=arr[i]
        
    temp=1
    for i in range(n-1,-1,-1):
        prod[i] *= temp
        temp*=arr[i]
        
    return prod
