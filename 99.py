def findPair(self, arr, L,n):
        arr.sort()
        size = L
  
        # Initialize positions of two elements
        i,j = 0,1
      
        # Search for a pair
        while i < size and j < size:
      
            if i != j and arr[j]-arr[i] == n:
                #print ("Pair found ",arr[i]," ",arr[j])
                return (1)
            elif arr[j] - arr[i] < n:
                j+=1
            else:
                i+=1
        
        return(-1)
