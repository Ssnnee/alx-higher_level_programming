#!/usr/bin/node

exports.esrever = function (list) {
  const ar = [];
  for (let i = list.length - 1; i >= 0; i--) {
    ar.push(list[i]);
  }
  return ar;
};
