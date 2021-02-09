#!/usr/bin/node
// function that returns the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  // console.log(list)
  // console.log(searchElement)

  let occurences = 0;
  for (let element = 0; element < list.length; element++) {
    if (list[element] === searchElement) {
      occurences = occurences + 1;
    }
  }
  return occurences;
};
