def threeWayPartition(self, arr, a, b):
	    s = 0
	    e = len(arr)-1
	    i= 0
	    
	    while(i<=e):
	        
	        if arr[i]<a:
	            temp = arr[i]
	            arr[i] = arr[s]
	            arr[s] = temp
	            i+=1
	            s+=1
	            
	        elif arr[i]>b:
	            temp = arr[i]
	            arr[i] = arr[e]
	            arr[e] = temp
	            e-=1
	            
	        else:
                i+=1
                
            #print(arr)
                
        return arr
