#!/usr/bin/node
// function that prints the number of arguments already printed and the new argument value.

let countArguments = 0;

exports.logMe = function (item) {
  console.log(`${countArguments}: ${item}`);
  countArguments = countArguments + 1;
};
