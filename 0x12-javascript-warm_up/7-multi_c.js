#!/usr/bin/node
const lst = process.argv;
if (isNaN(parseInt(lst[2]))) {
  console.log('Missing number of occurrences');
} else {
  for (let a = 0; a < parseInt(lst[2]); a++) {
    console.log('C is fun');
  }
}
