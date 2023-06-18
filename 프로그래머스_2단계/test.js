const ary1 = new Array(3);
const ary2 = Array(3)
  .fill(0)
  .map((_, i) => i);
const ary3 = [...new Array(3)];
const ary4 = [...Array(3)];
const ary5 = [, , ,];
const ary6 = [];
ary6.length = 3;
const ary7 = Array.from({ length: 3 }).map((v, i) => i);

console.log(ary1); //(3) [...]
console.log(ary2); //(3) [0,1,2]
console.log(ary3); // [undefined,undefined,undefined]
console.log(ary4); // [undefined,undefined,undefined]
console.log(ary5); //(3) [...]
console.log(ary6); //(3) [...]
console.log(ary7); // [undefined,undefined,undefined]

for (const el of ary2) {
  console.log(el);
}

