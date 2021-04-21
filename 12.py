# Time Complexity: O((n+m)*log(n+m))
# Space Complexity: O(1)

def merge(self, arr1, arr2, n, m): 
        i=0
        j=0
        k=n-1
        while i<=k and j<m:
            if arr1[i]<arr2[j]:
                i+=1
            else:
                temp = arr2[j]
                arr2[j] = arr1[k]
                arr1[k] = temp
                k-=1
                j+=1
                
        arr1.sort()
        arr2.sort()
