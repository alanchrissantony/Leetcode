/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    let dx={}
    for(let i=0; i<nums.length; i++){
        if(dx[nums[i]]){
            dx[nums[i]]+=1
        }else{
            dx[nums[i]]=1
        }
    }
    for(let el in dx){
        if(dx[el]==1){
            return parseInt(el)
        }
    }
};