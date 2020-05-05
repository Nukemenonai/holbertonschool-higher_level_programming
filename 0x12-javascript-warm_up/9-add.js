#!/usr/bin/node

function add (a, b) {
  let total = 0;
  if (a && b) {
    a = parseInt(a);
    b = parseInt(b);
  }

  if (!isNaN(a) && !isNaN(b)) {
    total = (a + b);
  } else {
    return NaN;
  }
  return total;
}

console.log(add(process.argv[2], process.argv[3]));
