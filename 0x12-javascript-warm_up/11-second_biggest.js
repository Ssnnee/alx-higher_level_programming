#!/usr/bin/node

const args = process.argv.slice(2);
const firstArg = args[2];
const sortedArgs = args.sort();
const argsLength = args.length;

if (isNaN(firstArg) || firstArg === 1) {
  console.log(0);
} else {
  console.log(sortedArgs[argsLength - 2]);
}
