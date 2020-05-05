#!/usr/bin/node

function factorial (x) {
  x = parseInt(x);
  if (isNaN(x)) {
    return 1;
  } else if (x <= 1) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}

if (!process.argv[2]) {
  process.argv[2] = NaN;
}

console.log(factorial(process.argv[2]));
