/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    let strArray = s.split('');
    let vowels = ['a', 'e', 'i', 'o', 'u'];
    let strVowels = [];
    let strConstant = [];
    for (let i = 0; i < strArray.length; i++) {
        if (vowels.includes(strArray[i])) {
            strVowels.push(strArray[i]);
        } else {
            strConstant.push(strArray[i]);
        }
    }
    for (let v in strVowels) {
        console.log(strVowels[v]);
    }
    for (let c in strConstant) {
        console.log(strConstant[c]);
    }
}

