#!/usr/bin/node
// gets the contents of a webpage and stores it in a file.
const fileSystem = require('fs');
const request = require('request');
const url = process.argv[2];
const nameFile = process.argv[3];

request.get(url, response);

function response (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fileSystem.writeFile(nameFile, body, handleError);
  }
}
function handleError (error) {
  if (error) {
    console.log(error);
  }
}
