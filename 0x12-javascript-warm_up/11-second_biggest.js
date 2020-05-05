#!/usr/bin/node

function secondBiggest (arr) {
  if (arr.length <= 1) {
    return 0;
  } else {
    arr.splice(arr.indexOf(Math.max.apply(null, arr)), 1);
    return (Math.max.apply(null, arr));
  }
}

process.argv.splice(0, 2);
const narray = process.argv.map(Number);
console.log(secondBiggest(narray));
