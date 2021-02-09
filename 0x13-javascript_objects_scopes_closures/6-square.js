#!/usr/bin/node
const Squaree = require('./5-square.js');

class Square extends Squaree {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let iter = 0; iter < this.height; iter++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
