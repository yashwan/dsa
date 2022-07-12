def getMax(nums,k):
    c=0
    k=len(nums)-k
    prev=sum(nums[k:])
    maxi=sum(nums[k:])
    j=k
    k+=1
    i=0
    print(prev)
    while k<len(nums):
       
        prev=prev-nums[j]+nums[i]
        maxi=max(maxi,prev)
        print(prev)
        i+=1
        j+=1
        k+=1
    print(maxi)
nums=[4,6,3,4]
getMax(nums,3)