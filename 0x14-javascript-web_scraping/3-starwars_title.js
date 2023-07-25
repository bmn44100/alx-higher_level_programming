#!/usr/bin/node

let request = require('request');
let request_url = 'http://swapi.co/api/films/';
let episode_number = process.argv[2];
request(request_url + episode_number, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  } else {
    console.log('Wrong status code');
  }
});
