#!/usr/bin/node
if (!process.argv[3].length <= 3) {
  console.log(0);
} else {
  console.log(Number(process.argv.sort().reverse()[1]));
}
