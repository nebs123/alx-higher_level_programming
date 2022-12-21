#!/usr/bin/node

const Square5 = require('./5-square.js');

class Square extends Square5 {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    let cr = 'X';
    if (c) {
      cr = c;
    }

    for (let x = 0; x < this.height; x++) {
      let str = '';
      for (let y = 0; y < this.width; y++) {
        str += cr;
      }
      console.log(str);
    }
  }
}

module.exports = Square;
