# Hackerearth Question 
# Uses a variant of Binary Search but a good question


n = int(input())
#arr1 = list(map(int,input().split()))
arr1 = []
for i in range(n):
    ele = int(input())
    arr1.append(ele)
arr1.sort()
t = int(input())
arr2 = []
for i in range(t):
    ele = int(input())
    arr2.append(ele)


pre = []
sum1 = 0

for i in arr1:
    sum1+=i
    pre.append(sum1)

def BinarySearch(arr,l,r,x):
    if r>=l:
        mid = (l+r)//2

        if arr[mid]==x:
            return BinarySearch(arr,mid+1,r,x)

        elif arr[mid] > x:
            return BinarySearch(arr,l,mid-1,x)
        
        else:
            return BinarySearch(arr,mid+1,r,x)
    else:
        return r


for i in arr2:
    
    temp = BinarySearch(arr1,0,n-1,i)

    print(temp+1,pre[temp])
        
    
    
















    
