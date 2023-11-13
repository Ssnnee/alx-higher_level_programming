#!/usr/bin/node

const args = process.argv.slice(2);
const firstArg = args[2];
const sortedArgs = args.sort();
const argsLength = args.length;

function checkNumbers (arr) {
  const positiveNumbers = arr.filter(num => num > 0);
  const negativeNumbers = arr.filter(num => num < 0);

  if (positiveNumbers.length === 1 && negativeNumbers.length >= 1) {
    return 1;
  } else if (positiveNumbers.length === 0 && negativeNumbers.length >= 1) {
    return 2;
  } else {
    return 0;
  }
}

if (isNaN(firstArg) || firstArg === 1) {
  console.log(0);
} else {
  if (checkNumbers(sortedArgs) === 1) {
    console.log(sortedArgs[0]);
  } else if (checkNumbers(sortedArgs) === 2) {
    console.log(sortedArgs[1]);
  } else {
    console.log(sortedArgs[argsLength - 2]);
  }
}
