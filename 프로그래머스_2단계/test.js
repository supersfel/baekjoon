const ary = new Array(10).fill().map((_) => [false, false, false, false]);

console.log(ary);

ary[0][2] = true;

console.log(ary);
