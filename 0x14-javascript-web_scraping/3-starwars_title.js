#!/usr/bin/node

let request = require('request');
let request_url = 'https://swapi-api.alx-tools.com/api/films/:id';
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
