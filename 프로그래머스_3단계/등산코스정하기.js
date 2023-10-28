class Heap {
  constructor() {
    this.heap = [0];
    this.length = 0;
  }

  getMax() {
    return this.heap[1] ? this.heap[1] : undefined;
  }

  swap(a, b) {
    [this.heap[a], this.heap[b]] = [this.heap[b], this.heap[a]];
  }

  push(value) {
    this.heap.push(value);
    this.length += 1;
    let idx = this.length;
    while (idx > 1) {
      const parentIdx = ~~(idx / 2);
      if (this.heap[parentIdx] >= this.heap[idx]) {
        this.swap(parentIdx, idx);
        idx = parentIdx;
      } else break;
    }
  }

  pop() {
    if (!this.length) return undefined;
    if (this.length === 1) {
      this.length--;
      return this.heap.pop();
    }
    const max = this.heap[1];

    this.heap[1] = this.heap.pop();
    this.length--;
    let idx = 1;

    while (idx < this.length) {
      const [leftIdx, rightIdx] = [idx * 2, idx * 2 + 1];

      let minIdx = 1;
      if (leftIdx > this.length) break;
      else if (rightIdx > this.length) minIdx = leftIdx;
      else
        minIdx = this.heap[leftIdx] <= this.heap[rightIdx] ? leftIdx : rightIdx;

      if (this.heap[idx] > this.heap[minIdx]) {
        this.swap(idx, minIdx);
        idx = minIdx;
      } else break;
    }
    return max;
  }
}

function solution(n, paths, gates, summits) {
  const graph = [...Array(n + 1)].map((v) => []);
  for (const [i, j, w] of paths) {
    graph[i].push([j, w]);
    graph[j].push([i, w]);
  }
  gates.sort();
  summits.sort();

  const summitMap = new Map();
  for (const summit of summits) summitMap.set(summit, true);

  let ret = [-1, Infinity];

  const queue = new Heap();
  const dp = Array(n + 1).fill(Infinity);
  for (const gate of gates) {
    queue.push(gate);
    dp[gate] = 0;
  }

  while (queue.length) {
    const node = queue.pop();
    const weight = dp[node];

    if (summitMap.get(node) || dp[node] < weight) continue;

    for (const [nextNode, newWeight] of graph[node]) {
      const newIntensity = Math.max(weight, newWeight);
      if (newIntensity < dp[nextNode]) {
        dp[nextNode] = newIntensity;
        queue.push(nextNode);
      }
    }
  }

  let answer = [0, Infinity];
  summits.sort((a, b) => a - b);
  for (const summit of summits) {
    if (dp[summit] < answer[1]) answer = [summit, dp[summit]];
  }

  return answer;
}
