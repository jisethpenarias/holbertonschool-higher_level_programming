#!/usr/bin/node
// executes x times a function.

module.exports.callMeMoby = function (number, theFunction) {
  for (let i = 0; i < number; i++) {
    theFunction();
  }
};
