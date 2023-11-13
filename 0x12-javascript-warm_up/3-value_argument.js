#!/usr/bin/node

const args = process.argv;
const firstArg = args[2];

if (isNaN(firstArg)) {
    console.log('Not argument');
}
console.log(firstArg);
