    #Time Complexity needs to be reduced. Current Time Complexity is O(n^3) and there are 6 comparisons in each loop which makes it worse.
def threeSum(nums):
    a=len(nums)
    i=0
    j=0
    k=0
    op=[]
    nums_negative=[]
    nums_positive=[]
    if 0 in nums:
        has_zero=True
    else:
        has_zero=False
    nums.sort()
    while i<a:
        if nums[i]<0:
            nums_negative.append(nums[i])
            j=j+1
        elif nums[i]>0:
            nums_positive.append(nums[i])
            k=k+1
        i=i+1

    print(nums_negative,nums_positive,has_zero,a)
    return op

threeSum([-1,0,1,2,-1,-4])