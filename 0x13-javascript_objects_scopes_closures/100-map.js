#!/usr/bin/node

const list = require('./100-data').list;

console.log(list.map((x) => x));
console.log(list.map((x, i) => x * i));
