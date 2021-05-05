#!/usr/bin/node
const request = require('request');
const UrlToGet = 'https://swapi-api.hbtn.io/api/films/';
const EpisodeId = process.argv[2];
request(UrlToGet + EpisodeId, function (err, response, body) {
  if (err) throw err;
  if (response.statusCode === 200) { console.log(JSON.parse(body).title); }
});
