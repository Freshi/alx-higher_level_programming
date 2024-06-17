#!/usr/bin/node
const { argv } = require('node:process');
if (!Number(argv[2])) {
  console.log('Missing number of occurrences');
} else {
  let count = Number(argv[2]);
  while (count > 0) {
    console.log('C is fun');
    count--;
  }
}
