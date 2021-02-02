#!/usr/bin/node
/*
Script that prints two arguments passed to it,
in the following format: “ is ”... contactenate arguments
*/

const args = process.argv;
console.log(`${args[2]} is ${args[3]}`);
