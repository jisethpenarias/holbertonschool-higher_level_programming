#!/usr/bin/node
/* prints the title of a Star Wars movie where
the episode number matches a given integer */

const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';

request((url + movieId), response);

function response (err, response, body) {
  err ? console.error(err) : console.log(JSON.parse(body).title);
}
