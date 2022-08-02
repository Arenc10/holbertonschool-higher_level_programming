#!/usr/bin/node
const args = process.argv.slice(2);
if (isNaN(args[0]) === false) {
  const n = parseInt(args[0]);
  console.log('My number: ' + n);
} else {
  console.log('Not a number');
}
