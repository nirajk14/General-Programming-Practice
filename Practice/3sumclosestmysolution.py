def threeSumClosestnums, target):
    nums.sort()
    bestSum=99999
    store=195
    for i,a in enumerate(nums):
        if i>0 and a==nums[i-1]:
            continue
        l,r=i+1,len(nums)-1
        while l<r:
            threeSum=a+nums[l]+nums[r]
            if abs(target-threeSum)<abs(target-bestSum):
                bestSum=threeSum
            if threeSum==target:
                return threeSum
                
            elif threeSum<target:
                l+=1
            else:
                r-=1
                
            
    
    return bestSum