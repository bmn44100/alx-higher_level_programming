#!/usr/bin/node
let myNumberArg = process.argv[2];
if (isNaN(myNumberArg)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myNumberArg);
}