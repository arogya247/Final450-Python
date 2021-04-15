def majorityElement(self, A):
        N =len(A)
        count=0
        candidate = 0
        for i in range(N):
            if A[i]==A[candidate]:
                count+=1
            else:
                count-=1
                
            if count==0:
                candidate = i
                count=1
        
        return A[candidate]
        
        ''' 
        count=0
        for i in A:
            if i==A[candidate]:
                count+=1
            
        if count>(N/2):
            return A[candidate]
        else:
            return -1
        '''
