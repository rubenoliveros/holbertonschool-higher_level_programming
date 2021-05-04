#!/usr/bin/node
const fs = require('fs');
const FileName = process.argv[2];
fs.readFile(FileName, 'utf-8', (err, data) => {
  if (err) throw err;
  console.log(data);
});
