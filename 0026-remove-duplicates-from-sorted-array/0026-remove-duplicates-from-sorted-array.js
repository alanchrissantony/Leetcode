/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    for(let i=1; i<nums.length; i++){
        if(nums[i]===nums[i-1]){
            nums.splice(i, 1)
            i--
        }
    }
};