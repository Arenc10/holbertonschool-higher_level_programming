#!/usr/bin/node
const { readFileSync, writeFileSync } = require('fs');

const firstFile = readFileSync('./' + process.argv[2], 'utf-8');
const secondFile = readFileSync('./' + process.argv[3], 'utf-8');
writeFileSync('./' + process.argv[4], firstFile + secondFile);
