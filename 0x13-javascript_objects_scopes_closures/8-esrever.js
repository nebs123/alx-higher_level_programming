#!/usr/bin/node

exports.esrever = function (list) {
  const reverse = [];
  for (let x = list.length - 1; x >= 0; x--) {
    reverse.push(list[x]);
  }
  return reverse;
};
