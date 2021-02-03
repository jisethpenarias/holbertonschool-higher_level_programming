#!/usr/bin/node
// script that computes and prints a factorial

const number = process.argv[2];
console.log(factorial(parseInt(number)));

function factorial (number) {
  if ( !number || number === 1) {
    return 1;
  }
    return number * factorial(number - 1);
}
