#!/usr/bin/node
/*
   a script that gets the contents of a
   webpage and stores it in a file
*/
let fs = require('fs');
let request = require('request');
let request_url = process.argv[2];
let file_path = process.argv[3];
request(request_url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    fs.writeFile(file_path, body, 'utf-8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  } else {
    console.log('Wrong status code');
  }
});
