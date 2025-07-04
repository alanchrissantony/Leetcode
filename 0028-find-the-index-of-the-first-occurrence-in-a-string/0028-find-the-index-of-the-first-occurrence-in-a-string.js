/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    n=needle.length
    let dx=haystack.slice(0, n)
    for(let i=0; i<=(haystack.length)-(n); i++){
        if(dx==needle){
            return i
        }
        dx=dx.slice(1) + haystack[n+i]
    }
    return -1
};