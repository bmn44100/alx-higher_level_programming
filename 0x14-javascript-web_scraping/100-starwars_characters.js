#!/usr/bin/node
/*
  a script that prints all characters of a Star Wars movie
*/
let request = require('request');
let movie_id = process.argv[2];
let request_url = 'http://swapi.co/api/films/' + movie_id;
request(request_url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    let starwars_characters = JSON.parse(body).characters;
    for (let c in starwars_characters) {
      let stars = starwars_characters[c];
      request(stars, function (err, response, body) {
        if (err) {
          console.log(err);
        } else {
          let current_star = JSON.parse(body);
          console.log(current_star.name);
        }
      });
    }
  } else {
    console.log('Wrong status code');
  }
});
