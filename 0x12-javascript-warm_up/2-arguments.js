#!/usr/bin/node
let numArg = process.argv.length - 2;
if (numArg < 1) {
  console.log("No argument");
} else if (numArg === 1) {
  console.log("Argument found");
} else {
  console.log("Arguments found");
}