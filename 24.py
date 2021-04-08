  def findLongestConseqSubseq(self,arr, N):       #first solution
      arr = list(set(arr))
      arr.sort()
      f = 0
      l = 0
      max1 = 1
      for i in range(1,len(arr)):
          if arr[i]-1 == arr[i-1]:
              l+=1
          else:
              max1 = max(max1,l-f+1)
              f = i
              l = i

      return max(max1,l-f+1)


def findLongestConseqSubseq(self,arr, n):          #second solution
        s = set()
        ans = 0
    
        # Hash all the array elements
        for ele in arr:
            s.add(ele)
    
        # check each possible sequence from the start
        # then update optimal length
        for i in range(n):
    
             # if current element is the starting
            # element of a sequence
            if (arr[i]-1) not in s:
    
                # Then check for next elements in the
                # sequence
                j = arr[i]
                while(j in s):
                    j += 1
    
                # update  optimal length if this length
                # is more
                ans = max(ans, j-arr[i])
        return ans
