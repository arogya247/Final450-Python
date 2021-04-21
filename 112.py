def kthElement(self,  arr1, arr2, n, m, x):
        
        i = 0
        j = 0
        k = n-1
        
        while(i<=k and j<m):
            if arr1[i] > arr2[j]:
                temp = arr1[k]
                arr1[k] = arr2[j]
                arr2[j] = temp
                k-=1
                j+=1
            else:
                i+=1
                
        # arr1.sort()
        # arr2.sort()
        # print(arr1)
        # print(arr2)
                
        if x<=n:
            arr1.sort()
            #print(arr1)
            return arr1[x-1]
        else:
            arr2.sort()
            #print(arr2)
            x-=n
            return arr2[x-1]
