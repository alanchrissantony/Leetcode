/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    let dx=""
    for(let el of digits){
        dx+=el
    }

    dx=(BigInt(dx)+1n).toString()

    let n=digits.length
    let m=dx.length
    if(n<m){
        digits.push(0)
    }
    for(let i=0; i<m; i++){
        if(dx[i] != digits[i]){
            digits[i]=parseInt(dx[i])
        }
    }
    return digits
    

};