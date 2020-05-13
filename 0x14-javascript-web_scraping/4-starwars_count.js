#!/usr/bin/node

const request = require('request');
const endpoint = process.argv[2];
const id = '18';

request(endpoint, function (err, response, body) {
  if (err) {
    console.error('error:', err);
  } else {
    const resp = JSON.parse(body);
    let count = 0;
    for (const i of resp.results) {
      for (const j of i.characters) {
        if (j.search(id) > 0) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
