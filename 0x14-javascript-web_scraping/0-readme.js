#!/usr/bin/node
// script that reads and prints the content of a file.

/* File System Object */
const fileSystem = require('fs');
const filePATH = process.argv[2];

/* Read File */
fileSystem.readFile(filePATH, 'utf-8', onFileReaded);

function onFileReaded (err, data) {
  /* If an error exists, show it, else show it data */
  err ? console.log(err) : console.log(data);
}
