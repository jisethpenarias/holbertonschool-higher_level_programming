#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || w === undefined || h <= 0 || h === undefined) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let iter = 0; iter < this.height; iter++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
