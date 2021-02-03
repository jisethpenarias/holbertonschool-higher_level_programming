#!/usr/bin/node
// Script that prints a square

const number = parseInt(process.argv[2]);

if (isNaN(number)) {
  console.log('Missing size');
} else {
  for (let iter = 0; iter < number; iter++) {
    console.log('X'.repeat(number));
  }
}
