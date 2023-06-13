#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let index = 0;
  for (let i in list) {
    if (list[i] === searchElement) {
      index++;
    }
  }
  return index;
};
