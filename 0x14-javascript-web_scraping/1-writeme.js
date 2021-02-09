#!/usr/bin/node
// writes a string to a file
const fileSystem = require('fs');
const filePATH = process.argv[2];
const fileText = process.argv[3];

fileSystem.writeFile(filePATH, fileText, 'utf-8', readTextFile);

function readTextFile (err) {
  if (err) {
    console.log(err);
  }
}
