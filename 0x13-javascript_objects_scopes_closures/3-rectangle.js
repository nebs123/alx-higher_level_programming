#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let x = 0; x < this.height; x++) {
      let str = '';
      for (let y = 0; y < this.width; y++) {
        str += 'X';
      }
      console.log(str);
    }
  }
}

module.exports = Rectangle;
