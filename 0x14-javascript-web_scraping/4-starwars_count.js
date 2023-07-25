#!/usr/bin/node
/*
  script that prints the number of movies
  where the character “Wedge Antilles” is present
*/
let request = require('request');
let request_url = process.argv[2];
request(request_url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    let movies = JSON.parse(body).results;
    let index = 0;
    for (let film in movies) {
      let character_ID = movies[film].characters;
      for (let character in character_ID) {
        if (character_ID[character].includes('18')) {
          index++;
        }
      }
    }
    console.log(index);
  } else {
    console.log('Wrong status code');
  }
});
