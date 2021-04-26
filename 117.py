# Time: O(1)
# Space: O(1)


def inSequence(self, A, B, C):
        
        if C==0:
            if B==A:
                return 1
            else:
                return 0
        
        x = (B-A)/C
        
        if x>=0 and (x%1)==0:
            return 1
        else:
            return 0
