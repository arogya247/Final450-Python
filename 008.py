## gfg
## Time: O(n)


##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,a,size):
        
        max_sum = -maxsize - 1
        max_sum_now = 0
        
        for i in a:
            max_sum_now += i
            max_sum = max(max_sum, max_sum_now)
            
            if max_sum_now < 0:
                max_sum_now = 0
            
        return max_sum
