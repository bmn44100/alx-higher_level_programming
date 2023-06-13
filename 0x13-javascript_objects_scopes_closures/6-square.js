#!/usr/bin/node
const inheritSquare = require('./5-square');
class Square extends inheritSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        console.log('c'.repeat(this.height));
      }
    }
  }
}
module.exports = Square;
