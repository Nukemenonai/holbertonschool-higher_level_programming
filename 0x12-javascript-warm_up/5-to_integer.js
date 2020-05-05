#!/usr/bin/node

if (process.argv[2]) {
  if (typeof (parseInt(process.argv[2]), 10) === 'number' &&
      isNaN(parseInt(process.argv[2])) === false) {
    console.log('My number: ' + parseInt(process.argv[2]));
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}
