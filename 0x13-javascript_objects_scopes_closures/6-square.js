#!/usr/bin/node
const Square5 = require('./5-square');

module.exports = class Square extends Square5 {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    const sym = c || 'X';
    for (let i = 0; i < this.size; i++) console.log(sym.repeat(this.size));
  }
};
