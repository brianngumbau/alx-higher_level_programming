#!/usr/bin/node
const square = require('./5-square');
class Square extends square {

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let a = 0; a < this.height; a++) {
      let s = '';
      for (let b = 0; b < this.width; b++) {
        s += c;
      }
      console.log(s);
    }
  }
}
module.exports = Square;
