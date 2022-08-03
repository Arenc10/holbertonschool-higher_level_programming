#!/usr/bin/node
const myList = require('./100-data').list
const newList = myList.map((el, index) => el * index);
console.log(myList);
console.log(newList);
