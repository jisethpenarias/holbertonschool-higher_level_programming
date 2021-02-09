#!/usr/bin/node
// class Rectangle that defines a rectangle
// this is bound to the new object being constructed.
class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
}
module.exports = Rectangle;
