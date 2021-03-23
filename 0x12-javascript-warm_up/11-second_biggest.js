#!/usr/bin/node
if (!process.argv[3]) {
  console.log(0);
} else {
  const unique = (value, index, self) => {
    return self.indexOf(value) === index;
  };
  console.log(process.argv.slice(2).filter(unique).sort().reverse()[1]);
}
