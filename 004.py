## gfg
## Time:O(n)

def sort012(self,arr,n):
        i = 0
        j = n-1
        
        x = 0
        
        while(x<=j):
            if arr[x]==0:
                arr[i],arr[x] = arr[x], arr[i]
                i+=1
                x+=1
            elif arr[x]==2:
                arr[j],arr[x] = arr[x],arr[j]
                j-=1
            else:
                x+=1
                
        return arr
