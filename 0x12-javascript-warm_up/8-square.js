#!/usr/bin/node
const args = process.argv.slice(2);
if (isNaN(args[0]) === false) {
  const n = parseInt(args[0]);
  for (let i = 0; i < n; i++) { console.log('X'.repeat(n)); }
} else {
  console.log('Missing size');
}
