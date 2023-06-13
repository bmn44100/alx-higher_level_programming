#!/usr/bin/node
let sizeSquare = process.argv[2];
if (isNaN(sizeSquare)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < sizeSquare; i++) {
    console.log('X'.repeat(sizeSquare));
  }
}