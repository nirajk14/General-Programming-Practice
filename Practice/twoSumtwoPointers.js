
const twoSum= (nums={},target) => {
    start=0;
    end=nums.length-1;
    result={}

    while (start<end) {
        sum= nums[start]+ nums[end];
        if (sum==target) {
            result[0]=start+1;
            result[1]=end+1;
            break;
        } else if (sum<target) start++;
        else end--;
    }
    return result;
}

console.log(twoSum([2,3,4],7))