#!/usr/bin/node
/* script that searches the second biggest
integer in the list of arguments. */

const number = process.argv;

if (number.length <= 3) {
  console.log(0);
} else {
  const numSecondBig = number.sort(function compare (a, b) { return b - a; });
  console.log(numSecondBig[3]);
}
