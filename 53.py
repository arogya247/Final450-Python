#  LEETCODE Question

  def countAndSay(self, n: int) -> str:

      def answer(n):
          i=0
          count=1
          arr = ""
          while(i<len(n)):

              if i==(len(n)-1) or n[i]!=n[i+1]:
                  arr+=str(count)
                  arr+=n[i]
                  count=1
                  i+=1
              elif n[i]==n[i+1]:
                  i+=1
                  count+=1

          return arr

      if n==1:
          return ("1")
      elif n==2:
          return ("11")
      else:
          temp = self.countAndSay(n-1)
          return answer(temp)

