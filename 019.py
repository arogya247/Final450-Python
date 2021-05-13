def commonElements (self,A, B, C, n1, n2, n3):
        p=0
        q=0
        r=0
        arr1 = []
        while(p<n1 and q<n2 and r<n3):
            if A[p]==B[q] and B[q]==C[r]:
                arr1.append(A[p])
                p+=1
                q+=1
                r+=1
            elif A[p]<B[q]:
                p+=1
            elif B[q]<C[r]:
                q+=1
            else:
                r+=1
            
        return sorted(list(set(arr1)))
