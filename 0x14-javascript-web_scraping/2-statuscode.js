#!/usr/bin/node
// display the status code of a GET request.

const request = require('request');
const url = process.argv[2];

request(url, response);

function response (err, response) {
  err ? console.error(err) : console.log('code:', response.statusCode); // 200
}
