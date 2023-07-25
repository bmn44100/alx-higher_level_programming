#!/usr/bin/node
/*
  a script that display the status code of a GET request
*/
let request = require('request');
let request_url = process.argv[2];
request(request_url, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
