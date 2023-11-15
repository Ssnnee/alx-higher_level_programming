#!/usr/bin/node

const dict = require('./101-data').dict;

const userIdsByOccurrence = Object.entries(dict)
  .reduce((acc, [id, occ]) => {
    acc[occ] = acc[occ]
      ? [...acc[occ], id]
      : [id];
    return acc;
  }, {});

console.log(userIdsByOccurrence);
