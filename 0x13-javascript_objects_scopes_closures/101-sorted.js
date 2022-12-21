#!/usr/bin/node

const dict = require('./101-data.js').dict;

const newDict = {};

const data = Object.entries(dict);
data.forEach(([key, value]) => {
  if (newDict[value.toString()]) {
    newDict[value.toString()].push(key.toString());
  } else {
    newDict[value.toString()] = [key.toString()];
  }
});

console.log(newDict);
