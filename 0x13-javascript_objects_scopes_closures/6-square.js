#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let char = 'X';
    if (c) {
      char = c;
    }

    for (let x = 0; x < this.height; x++) {
      let str = '';
      for (let y = 0; y < this.width; y++) {
        str += char;
      }
      console.log(str);
    }
  }
}

module.exports = Square;
