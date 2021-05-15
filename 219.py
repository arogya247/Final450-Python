# GFG
# Expected Time Complexity : O(N*LogN)
# Expected Auxilliary Space : O(N)



def maximumMeetings(self,n,start,end):

    list1 = sorted(list(zip(end,start)))

    f = list1[0]
    count=1
    for i in list1:
        if f[0] < i[1]:
            count+=1
            f = i


    return count
