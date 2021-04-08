def find3Numbers(self,A, n, X):
        for i in range(0, n-1):
        # Find pair in subarray A[i + 1..n-1] 
        # with sum equal to sum - A[i]
            s = set()
            curr_sum = X - A[i]
            for j in range(i + 1, n):
                if (curr_sum - A[j]) in s:
                    #print("Triplet is", A[i], 
                    #        ", ", A[j], ", ", curr_sum-A[j])
                    return True
                s.add(A[j])
    
        return False
