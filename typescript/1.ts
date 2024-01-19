function twoSum(nums: number[], target: number) {
    const dict = {};

    for(let i = nums.length; i >= 0; i--) {
        if(dict.hasOwnProperty(nums[i])) {
            return [dict[nums[i]], i];
        }

        dict[target - nums[i]] = i;
    }
};