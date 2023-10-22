function solution(beginning, target) {
  const map = [...Array(beginning.length)].map((_) =>
    Array(beginning[0].length).fill(false)
  );
  const rLen = beginning.length;
  const cLen = beginning[0].length;

  for (let i = 0; i < rLen; i++) {
    for (let j = 0; j < cLen; j++) {
      if (beginning[i][j] !== target[i][j]) map[i][j] = !map[i][j];
    }
  }

  const changeRow = (n) => {
    for (let i = 0; i < cLen; i++) map[n][i] = !map[n][i];
  };
  const changeCol = (n) => {
    for (let i = 0; i < rLen; i++) map[i][n] = !map[i][n];
  };

  let ret = 0;
  for (let i = 0; i < cLen; i++) {
    if (map[0][i]) {
      changeCol(i);
      ret++;
    }
  }
  for (let i = 0; i < rLen; i++) {
    if (map[i][0]) {
      changeRow(i);
      ret++;
    }
  }

  for (let i = 0; i < rLen; i++) {
    for (let j = 0; j < cLen; j++) {
      if (map[i][j]) return -1;
    }
  }
  return ret;
}
