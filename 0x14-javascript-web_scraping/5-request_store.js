#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const UrlToGet = process.argv[2];
const FilePath = process.argv[3];
request(UrlToGet, function (err, response, body) {
  if (err) throw err;
  fs.writeFile(FilePath, body, 'utf-8', function (err) {
    if (err) throw err;
  });
});
