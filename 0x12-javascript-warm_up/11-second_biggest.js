#!/usr/bin/node
/* script that searches the second biggest
integer in the list of arguments. */

console.log(process.argv.length <= 3 ? 0 : process.argv.sort(function compare (a, b) { return b - a; })[3]);
