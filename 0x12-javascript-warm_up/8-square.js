#!/usr/bin/node

if (process.argv[2] && isNaN(process.argv[2] === false)) {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('X'.repeat(process.argv[2]));
  }
} else {
  console.log('Missing size');
}
