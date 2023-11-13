#!/usr/bin/node

const args = process.argv;
const firstArg = args[2];

if (firstArg === undefined) {
  console.log('Not argument');
} else {
  console.log(firstArg);
}
