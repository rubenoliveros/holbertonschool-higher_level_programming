#!/usr/bin/node
const request = require('request');
const FilmId = process.argv[2];
const UrlToGet = 'http://swapi.co/api/people/';
request(UrlToGet, function (err, response, body) {
  if (err) throw err;
  if (response.statusCode === 200) {
    const name = JSON.parse(body).results.name;
    const films = JSON.parse(body).results.films;
    for (const i of films) {
      if (i.includes(`https://swapi-api.hbtn.io/api/films/${FilmId}/`)) {
        console.log(name[i]);
      }
    }
  }
});
