#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const results = JSON.parse(body);
    const toPrint = {};

    for (const element of results) {
      const userID = element.userId;
      const taksCompleted = element.completed;

      if (taksCompleted && !toPrint[userID]) {
        toPrint[userID] = 0;
      }

      if (taksCompleted) {
        toPrint[userID] += 1;
      }
    }
    console.log(toPrint);
  }
});
