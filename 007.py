def rotate( arr, n):
    
    arr[0],arr[n-1] = arr[n-1],arr[0]
    
    for i in range(n-1,1,-1):
        arr[i],arr[i-1] = arr[i-1],arr[i]
        
    return arr
