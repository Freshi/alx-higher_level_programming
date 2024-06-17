#!/usr/bin/node
const { argv } = require('node:process');
if (argv.length <= 3) {
  console.log(0);
} else {
  const args = argv.map(x => Number(x));
  console.log(args.sort((a, b) => a - b).reverse()[1]);
}
