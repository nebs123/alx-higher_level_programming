#!/usr/bin/node

let first = -Infinity;
let second = -Infinity;

if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  for (let x = 2; x < process.argv.length; x++) {
    if (parseInt(process.argv[x]) > first) {
      second = first;
      first = parseInt(process.argv[x]);
    } else if (parseInt(process.argv[x]) > second) {
      second = parseInt(process.argv[x]);
    }
  }
  console.log(second);
}
