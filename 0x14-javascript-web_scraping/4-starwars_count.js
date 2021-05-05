#!/usr/bin/node
const request = require('request');
const UrlToGet = process.argv[2];
const ID = '18';
request(UrlToGet, function (err, response, body) {
  if (err) throw err;
  if (response.statusCode === 200) {
    let WedgeAntillesCount = 0;
    const films = JSON.parse(body).results;
    for (const i of films) {
      if (i.characters.includes(`https://swapi-api.hbtn.io/api/people/${ID}/`)) {
        WedgeAntillesCount++;
      }
    }
    console.log(WedgeAntillesCount);
  }
});
