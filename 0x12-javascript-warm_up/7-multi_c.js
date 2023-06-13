#!/usr/bin/node
let numIter = process.argv[2];
let iLoveC = 'C is fun';
if (isNaN(numIter)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < numIter; i++) {
    console.log(iLoveC);
  }
}