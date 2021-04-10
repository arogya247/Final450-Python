def sb(self, a, n, x):
        # Your code goes here 
        l = 0 
        r = 0
        min1 = n
        while(r<n):
            if sum(a[l:r+1])<=x:
                r+=1
            elif sum(a[l:r+1])>x:
                min1 = min(min1,r-l+1)
                #print(min1)
                l+=1
                
        return min1
