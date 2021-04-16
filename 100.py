##  Time = O(n^3)
##  Space = O(1)
##  Two pointer solution

def fourSum(self, arr, k):
        arr.sort()
        L = len(arr)
        Arr = []
        for i in range(L-3):
            if i and arr[i] == arr[i - 1]:
                continue
            for j in range(i+1,L-2):
                if j != i + 1 and arr[j] == arr[j - 1]:
                    continue
                l = j+1
                r = L-1
                
                while(l<r):
                    if (arr[l] + arr[r]) == (k - arr[i] - arr[j]):
                        Arr.append([arr[i],arr[j],arr[l],arr[r]])
                        l+=1
                        r-=1
                        while (l < r and arr[l] == arr[l - 1]):
                            l+=1
                        while (l < r and arr[r] == arr[r + 1]): 
                            r-=1
                    elif (arr[l]+arr[r]) < (k - arr[i] - arr[j]):
                        l+=1
                    else:
                        r-=1        
        return (Arr)
