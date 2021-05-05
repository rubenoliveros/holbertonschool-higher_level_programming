#!/usr/bin/node
const request = require('request');
const UrlToGet = process.argv[2];
const WedgeAntillesUrl = 'https://swapi-api.hbtn.io/api/people/18/';
request(UrlToGet, function (err, response, body) {
  if (err) throw err;
  if (response.statusCode === 200) {
    let WedgeAntillesCount = 0;
    const films = JSON.parse(body).results;
    for (const i in films) {
      if (films[i].characters.includes(WedgeAntillesUrl)) {
        WedgeAntillesCount++;
      }
    }
    console.log(WedgeAntillesCount);
  }
});
