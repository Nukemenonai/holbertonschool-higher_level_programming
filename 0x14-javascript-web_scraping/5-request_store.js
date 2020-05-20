#!/usr/bin/node

const fs = require('fs');
const request = require('request');

request(process.argv[2], function (err, res, body) {
  fs.writeFile(process.argv[3], body, (err) => {
    if (err) {
      console.error(err);
    }
  });
  if (err) {
    console.error(err);
  }
});
