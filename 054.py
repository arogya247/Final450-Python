# GFG
# Expected Time Complexity: O(|S|2)
# Expected Auxiliary Space: O(1)

def longestPalin(self, S):
        
        start = 0
        end = 1
        
        for i in range(1,len(S)):
            
            # even string
            
            l = i-1
            h = i
            
            while(l>=0 and h<len(S) and S[l]==S[h]):
                
                if h-l+1 > end:
                    start = l
                    end = h-l+1
                    
                l-=1
                h+=1
                
                
            # odd string
            
            l = i-1
            h = i+1
            
            while(l>=0 and h<len(S) and S[l]==S[h]):
                
                if h-l+1 > end:
                    start = l
                    end = h-l+1
                    
                l-=1
                h+=1
                
                
        return(S[start:start+end])
