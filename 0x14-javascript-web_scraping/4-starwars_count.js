#!/usr/bin/node

const request = require('request');
const endpoint = process.argv[2];
const wedge = 'https://swapi-api.hbtn.io/api/people/18/';

request(endpoint, function (error, response, body) {
  if (error === null) {
    let ct = 0;
    const resp = JSON.parse(body);
    for (let i = 0; i < resp.results.length; i++) {
      for (let j = 0; j < resp.results[i].characters.length; j++) {
        if (wedge === resp.results[i].characters[j]) {
          ct++;
        }
      }
    }
    console.log(ct);
  }
  if (error) {
    console.log(error);
  }
});
