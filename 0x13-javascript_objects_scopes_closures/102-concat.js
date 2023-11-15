#!/usr/bin/node

const args = process.argv.slice(2);
const fs = require('fs');
const fileAPath = args[0];
const fileBPath = args[1];
const destinationPath = args[2];

const fileContentA = fs.readFileSync(fileAPath, 'utf8');
const fileContentB = fs.readFileSync(fileBPath, 'utf8');
const concatenatedContent = fileContentA + fileContentB;
fs.writeFileSync(destinationPath, concatenatedContent);
