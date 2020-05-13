#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const resp = JSON.parse(body);
    const dict = {};
    for (const i of resp) {
      if (i.completed === true) {
        if (dict[i.userId] === undefined) {
          dict[i.userId] = 0;
        }
        dict[i.userId] += 1;
      }
    }
    console.log(dict);
  }
});
