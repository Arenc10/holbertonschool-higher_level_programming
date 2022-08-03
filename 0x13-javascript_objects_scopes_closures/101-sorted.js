#!/usr/bin/node
const myDict = require('./101-data').dict;
const myObj = {};
for (const key in myDict) {
  if (!Object.prototype.hasOwnProperty.call(myObj, myDict[key])) {
    myObj[myDict[key]] = [];
  }
}
for (const key in myDict) {
  if (Object.prototype.hasOwnProperty.call(myObj, myDict[key])) {
    myObj[myDict[key]].push(key);
  }
}
console.log(myObj);
