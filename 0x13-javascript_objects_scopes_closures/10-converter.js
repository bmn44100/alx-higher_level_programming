#!/usr/bin/node
exports.converter = function (base) {
  return function (conv) {
    return conv.toString(base);
  };
};
