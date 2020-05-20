#!/usr/bin/node

exports.converter = function (base) {
  return function baseConvert (number) {
    return parseInt(number + '', 10).toString(base);
  };
};
