#!/usr/bin/node
// Script that prints the addition of 2 integers

const numOne = process.argv[2];
const numTwo = process.argv[3];
console.log(add(numOne, numTwo));

function add (a, b) {
  return parseInt(a) + parseInt(b);
}
