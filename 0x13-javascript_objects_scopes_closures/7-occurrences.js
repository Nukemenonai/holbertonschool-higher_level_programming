#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let oc = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      oc++;
    }
  }
  return oc;
};
