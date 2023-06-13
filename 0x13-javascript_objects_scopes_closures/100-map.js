#!/usr/bin/node
const list = require('./100-data').list;
let mapList = list.map((current, index) => {
  return (current * index);
});
console.log(list);
console.log(mapList);
