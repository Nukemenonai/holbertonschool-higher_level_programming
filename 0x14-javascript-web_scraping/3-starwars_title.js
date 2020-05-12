#!/usr/bin/node

const request = require('request');
const endpoint = 'https://swapi-api.hbtn.io/api/films/';

request(endpoint + process.argv[2], function (error, response, body) {
  if (error === null) {
    const resp = JSON.parse(body);
    console.log(resp.title);
  }
  if (error) {
    console.log(error);
  }
});
