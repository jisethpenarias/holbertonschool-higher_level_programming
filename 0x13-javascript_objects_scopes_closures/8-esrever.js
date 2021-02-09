#!/usr/bin/node
// function that returns the reversed version of a list

exports.esrever = function (list) {
  const newList = [];
  for (let iter = list.length, element = 0; iter > 0; iter--, element++) {
    newList[element] = list[iter - 1];
  }
  return newList;
};
