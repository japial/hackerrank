function diagonalDifference(arr) {
    let mainSum = 0, secondarySum = 0;
    let arrSize = arr.length;
    for (let row = 0; row < arrSize; row++) {
        mainSum = mainSum + arr[row][row];
        secondarySum = secondarySum + arr[row][arrSize - row - 1];
    }
    let result = mainSum - secondarySum;
    return Math.abs(result);
}

let arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]];
let result = diagonalDifference(arr);
console.log(result);