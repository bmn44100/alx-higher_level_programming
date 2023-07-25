#!/usr/bin/node
/*
  a script that reads and prints the content of a file
*/
let fs = require('fs');
let file_path = process.argv[2];
let content = process.argv[3];
fs.writeFile(file_path, content, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
