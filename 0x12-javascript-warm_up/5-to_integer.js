#!/usr/bin/node

const args = process.argv;
const firstArg = args[2];

if (isNaN(firstArg)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(firstArg, 10));
}
