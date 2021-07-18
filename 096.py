def findTwoElement( self,arr, n): 
        res = []
        for i in range(n):
            if arr[abs(arr[i])-1]>0:
                arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
            else:
                res.append(abs(arr[i]))
                
        for i in range(n):
            if arr[i]>0:
                res.append(i+1)
                
        return res
