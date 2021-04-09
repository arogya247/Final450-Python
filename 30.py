def findMinDiff(self, A,N,M):
    
        A.sort()
        
        if N<M:
            return(-1)
        
        l = 0
        r = M-1
        min1 = A[N-1] - A[0]
        
        while(r<N):
            min1 = min(min1,A[r]-A[l])
            #print(l," ",r," ",min1)
            l+=1
            r+=1
            
        return min1
