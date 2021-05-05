#!/usr/bin/node
const request = require('request');
const UrlToGet = process.argv[2];
const WedgeAntilles = 18;
request(UrlToGet, function (err, response, body) {
  if (err) throw err;
  if (response.statusCode === 200) {
    let WedgeAntillesCount = 0;
    const films = JSON.parse(body).results;
    for (const i in films) {
      if (films[i].characters.includes(`https://swapi-api.hbtn.io/api/people/${WedgeAntilles}/`)) {
        WedgeAntillesCount++;
      }
    }
    console.log(WedgeAntillesCount);
  }
});
