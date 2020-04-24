
/*
 * Create the function factorial here
 */
function factorial(n) {
    let fact = 0;
    if (n > 0) {
        fact = n;
        for (let i = 1; i < n; ++i) {
            fact = fact * i;
        }
        return fact;
    }
}
