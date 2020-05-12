#!/usr/bin/node

const list1 = require('./100-data').list;
const map1 = list1.map(x => x * list1.indexOf(x));

console.log(list1);
console.log(map1);
