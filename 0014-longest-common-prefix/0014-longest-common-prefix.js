/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    for(let i=strs[0].length; i>0; i--){
        let flag=true
        dx=strs[0].slice(0,i)
        for(let j=1; j<strs.length; j++){
            if(dx!=strs[j].slice(0, i)){
                flag=false
                break
            }
        }
        if(flag){
            return dx
        }
    }
    return ""
   
};