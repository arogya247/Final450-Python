## GFG
# Expected Time Complexity: O(|x|)
# Expected Auixilliary Space: O(|x|)



#Function to check if brackets are balanced or not.
    def ispar(self,x):
        a = "{(["
        b = "})]"
        temp = ""
        for i in x:
            #print(temp)
            if i in a:
                temp+=i
            else:
                if len(temp)==0:
                    return False
                elif (temp[-1]=="[" and i=="]") or (temp[-1]=="(" and i==")") or (temp[-1]=="{" and i=="}"):
                    temp = temp[:-1]
                else:
                    #print(temp[-1]," ", i)
                    return False
                
                    
        if len(temp)!=0:
            return False
        else:
            return True
