#!/usr/bin/node

const log = [];
exports.logMe = function (item) {
  log.push(item);
  console.log(log.indexOf(item) + ': ' + item);
};
