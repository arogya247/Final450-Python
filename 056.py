## Recursion Solution

def answer(str1, sbstr):
    
    if len(str1)==0:
        print(sbstr)
        return 
    
    answer(str1[1:], sbstr + str1[0])
    answer(str1[1:], sbstr)
    
    
    
answer("abc", "")
