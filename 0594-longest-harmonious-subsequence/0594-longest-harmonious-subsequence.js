/**
 * @param {number[]} nums
 * @return {number}
 */
var findLHS = function(nums) {
    let dt = {}
    for(let el of nums){
        if(dt[el]){
            dt[el]+=1
        }else{
            dt[el]=1
        }
    }
    let mx=0
    let dx=0
    for(let el of Object.keys(dt)){
        dx=parseInt(el)+1
        if(dt[dx]){
            mx=Math.max(mx, dt[el]+dt[dx])
        }
    }
    return mx
};