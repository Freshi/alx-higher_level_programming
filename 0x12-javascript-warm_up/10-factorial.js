#!/usr/bin/node
const { argv } = require('node:process');
function factorial (num) {
  if (isNaN(num) || num <= 0) {
    return 1;
  } else {
    return (num * factorial(num - 1));
  }
}
console.log(factorial(Number(argv[2])));
