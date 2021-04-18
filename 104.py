#  Time: O(n)
#  Space: O(n)

#Function to count subarrays with sum equal to 0.
    def findSubArrays(self,arr,n):
        
        arr2 = {}
        sum1 = 0
        count=0
        for i in range(n):
            
            sum1+=arr[i]
            if sum1==0:
                count+=1
            if sum1 not in arr2:
                arr2[sum1] = 1
            else:
                temp = arr2.get(sum1)
                count+=temp
                arr2[sum1] = temp+1
        return count
