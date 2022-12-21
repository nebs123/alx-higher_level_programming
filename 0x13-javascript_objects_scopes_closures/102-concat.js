#!/usr/bin/node

const fs = require('fs/promises');

(async () => {
  try {
    const data1 = await fs.readFile(process.argv[2], { encoding: 'utf8' });
    const data2 = await fs.readFile(process.argv[3], { encoding: 'utf8' });
    await fs.writeFile(process.argv[4], data1, { encoding: 'utf8' });
    await fs.appendFile(process.argv[4], data2, { encoding: 'utf8' });
  } catch (err) {
    console.log(err);
  }
})();
