#!/usr/bin/node
/*
  a script that reads and prints the content of a file
*/
let fs = require('fs');
let file_path = process.argv[2];
fs.readFile(file_path, 'utf-8', (err, content) => {
  if (err) {
    console.log(err);
  } else {
    console.log(content);
  }
});
