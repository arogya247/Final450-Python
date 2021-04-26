# Time:  O(nlogn)
## This solution is not getting accepted on spoj but this is the correct way

N,K = map(int,input().split())
Arr = list(map(int,input().split()))
#import time

def check(arr,mx):
        sum1=0
        for i in arr:
            if i>mx:
                sum1+=(i-mx)
        return sum1


def answer(arr,n,k):
    
    start = min(arr)
    end = max(arr)
    res=0
    while(start<=end):
        mid = (start+end)//2
        temp = check(arr,mid)
        #print("Mid:   ",mid)
        #print("Temp:  ",temp)
        #time.sleep(3)
        if temp>=k:
            start=mid+1
            res = mid
        elif temp<k:
            end=mid-1

    return (res)


#N = 4
#K = 7
#Arr = [20,15,10,17]
print(answer(Arr,N,K))
