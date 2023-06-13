#!/usr/bin/node
let factArg = parseInt(process.argv[2]);
let x = factArg;
function factorial (x) {
  if (x === 1 || isNaN(x)) {
    return (1);
  } else {
    return (x * factorial(x - 1));
  }
}
console.log(factorial(x));