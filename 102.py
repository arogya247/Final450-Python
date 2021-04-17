def countTriplets(self,arr, n, x):
        arr.sort()
        count=0
        for i in range(n-2):
            l = i+1
            r = n-1
            
            while(l<r):
                
                # If sum of current triplet is more or equal,
                # move right corner to look for smaller values
                if (arr[i]+arr[l]+arr[r] >=x):
                    r-=1
                
                # Else move left corner
                else:
                    
                    # This is important. For current i and j, there
                    # can be total k-j third elements.
                    count += (r - l)
                    l+=1
                        
        return count
