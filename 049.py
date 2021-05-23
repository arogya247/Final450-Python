def answer(string):
    
    dict1 = {}
    
    for i in string:
        
        if i in dict1:
            dict1[i]+=1
        else:
            dict1[i]=1

    return dict1





str1 = "aabdccaedbbb"

print(answer(str1))
