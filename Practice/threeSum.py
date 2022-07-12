    #Time Complexity needs to be reduced. Current Time Complexity is O(n^3) and there are 6 comparisons in each loop which makes it worse.
def threeSum(nums):
    a=len(nums)
    i=0
    j=0
    k=0
    op=[]
    while i<a:
        j=i+1
        while j<a:
            k=j+1
            while k<a:
                if nums[i]+nums[j]+nums[k]==0 and ([nums[i],nums[j],nums[k]] not in op and [nums[j],nums[k],nums[i]] not in op) and ([nums[k],nums[i],nums[j]] not in op) and ([nums[k],nums[j],nums[i]] not in op) and ([nums[i],nums[k],nums[j]] not in op) and (([nums[j],nums[i],nums[k]] not in op)):
                    op.append([nums[i],nums[j],nums[k]])
                k=k+1
            j=j+1
        i=i+1
    return op

#threeSum([-1,0,1,2,-1,-4])