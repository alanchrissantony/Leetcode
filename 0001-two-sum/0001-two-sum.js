/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    for(let i=0; i<nums.length; i++){
        let arr=nums.slice(i+1)
        if(arr.includes(target-nums[i])){
            return [i, arr.indexOf(target-nums[i])+i+1]
        }
    }
    return -1
};