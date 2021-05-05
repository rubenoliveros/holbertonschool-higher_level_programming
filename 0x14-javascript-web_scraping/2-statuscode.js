#!/usr/bin/node
const request = require('request');
const UrlToGet = process.argv[2];
request(UrlToGet, function (err, response) {
  if (err) throw err;
  console.log('code: ', response && response.statusCode);
});
