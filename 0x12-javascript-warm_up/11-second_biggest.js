#!/usr/bin/node
let listArgs = process.argv;
if (listArgs.length <= 3) {
  console.log(0);
} else {
  console.log(listArgs.sort().reverse()[1]);
}