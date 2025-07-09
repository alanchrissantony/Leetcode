/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {

    for(let i=0; i<arr.length; i++){
        let dp=arr.splice(i,size)
        arr.splice(i,0,dp)
    }
    return arr
};
