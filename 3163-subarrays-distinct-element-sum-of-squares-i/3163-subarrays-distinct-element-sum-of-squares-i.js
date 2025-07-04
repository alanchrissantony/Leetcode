/**
 * @param {number[]} nums
 * @return {number}
 */
var sumCounts = function(nums) {
    const n=nums.length
    let dx=0
    for(let i=0; i<n; i++){
        let s=new Set()
        for(let j=i; j<n; j++){
            s.add(nums[j])
            dx+=s.size**2
        }
    }
    return dx
};