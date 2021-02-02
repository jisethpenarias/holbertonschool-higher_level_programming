#!/usr/bin/node
// Script that prints x times “C is fun”

const args = process.argv[2];

if (isNaN(args)) {
  console.log('Missing number of occurrences');
} else {
  for (let iter = 0; iter < Number(args); iter++) {
    console.log('C is fun');
  }
}
