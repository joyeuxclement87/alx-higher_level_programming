#!/usr/bin/node
const n = process.argv.length;
if (n <= 3) {
  console.log(0);
} else {
  const ar = process.argv.slice(2);
  const arInt = ar.sort((j, h) => j - h);
  console.log(arInt[arInt.length - 2]);
}
