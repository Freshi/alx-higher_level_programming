#!/usr/bin/env node
const { argv } = require('node:process');
if (argv.length <= 3) {
  console.log(0);
} else {
 let args = argv.map( x => Number(x));
  console.log(args.sort((a, b) => a - b).at(-2));
}
