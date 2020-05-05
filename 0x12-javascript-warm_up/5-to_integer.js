#!/usr/bin/node

if (process.argv[2]) {
  if (typeof (parseInt(process.argv[2])) === 'number') {
    console.log('My number: ' + parseInt(process.argv[2]));
  }
} else {
  console.log('Not a number');
}
