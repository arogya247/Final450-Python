## GFG
## Time Complexity: 

def findDuplicate(self, arr: List[int]) -> int:
        
        size = len(arr)
        
        for i in range(0, size):
 
            if arr[abs(arr[i])] >= 0:
                arr[abs(arr[i])] = -arr[abs(arr[i])]
            else:
                return(abs(arr[i]))
