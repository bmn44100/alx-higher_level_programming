#!/usr/bin/node
let firstArg = parseInt(process.argv[2]);
let secondArg = parseInt(process.argv[3]);
let a = firstArg;
let b = secondArg;
function add (a, b) {
  return (a + b);
}
console.log(add(a, b));