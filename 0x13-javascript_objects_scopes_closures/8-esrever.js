#!/usr/bin/node

exports.esrever = function (list) {
  const nl = [];
  for (let i = list.length - 1; i >= 0; i--) {
    nl.push(list[i]);
  }
  return nl;
};
