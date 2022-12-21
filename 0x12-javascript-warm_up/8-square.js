#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < num; x++) {
    for (let y = 0; y < num; y++) {
      process.stdout.write('X');
    }
    process.stdout.write('\n');
  }
}
