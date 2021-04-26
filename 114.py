#  Book allocation problem

class Solution:
    def findPages(self,arr, n, m):
        # n: no of book
        # m: no of students
        
        if m==1:
            return sum(arr)
        
        def isValid(arr,n,m,mx):
            count=1
            sum1=0
            for i in range(n):
                
                sum1+=arr[i]
                if sum1>mx:
                    sum1=arr[i]
                    count+=1
                
                if count>m:
                    return False
            
            return True
            
            
        
        start = max(arr)
        end = sum(arr)
        res = -1
        
        while(start<=end):
            mid = (start+end)//2
            
            if (isValid(arr,n,m,mid))==True:
                res = mid
                end = mid-1
            else:
                start = mid+1
                
        
        return res  
            
        
        
        #return: the expected answer if possible else return -1


