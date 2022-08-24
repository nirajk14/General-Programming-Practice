
def twoSum(self,nums, target):
    hash_table = {}
    for i in range(len(nums)):
        
        if nums[i] in hash_table:
            print (i,hash_table,'up')
            return [hash_table[nums[i]], i]
            
        else:
            hash_table[target - nums[i]] = i
            print (i,hash_table)