#!/usr/bin/node
/*
   a script that prints all characters
   of a Star Wars movie
*/
let request = require('request');
let movie_id = process.argv[2];
let request_url = 'http://swapi.co/api/films/' + movie_id;
request(request_url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    let starwars = {};
    let stars = JSON.parse(body).characters;
    for (let c in stars) {
      request(stars[c], function (err, response, body) {
        if (err) {
          console.log(err);
        } else {
          starwars[c] = JSON.parse(body).name;
        }
        if (stars.length === Object.keys(starwars).length) {
          for (let key in starwars) {
            console.log(starwars[key]);
          }
        }
      });
    }
  } else {
    console.log('Wrong status code');
  }
});
