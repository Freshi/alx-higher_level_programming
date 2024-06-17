#!/usr/bin/node
const { argv } = require('node:process');
if (!Number(argv[2])) {
  console.log('Missing size');
} else {
  let width = Number(argv[2]);
  let height = Number(argv[2]);
  let row = '';
  while (width > 0) {
    row += 'X';
    width--;
  }
  while (height > 0) {
    console.log(row);
    height--;
  }
}
