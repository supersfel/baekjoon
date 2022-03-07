import sys

n = int(sys.stdin.readline())
heap = [ 0 ]
idx = 0




for _ in range(n):
    i = int(sys.stdin.readline())
    if i == 0 :
        if idx ==0:
            print(0)
        elif idx ==1:
            print(heap.pop())
            idx-=1
        else:
            print(heap[1])
            heap[1] = heap.pop()
            idx -=1

            tmp_idx = 1
            while tmp_idx*2 <= idx:

                if heap[tmp_idx] < heap[tmp_idx * 2]:
                    heap[tmp_idx], heap[tmp_idx * 2] = heap[tmp_idx * 2], heap[tmp_idx]

                if tmp_idx*2+1 <= idx and heap[tmp_idx] < heap[tmp_idx*2 + 1]:
                    heap[tmp_idx], heap[tmp_idx * 2+1] = heap[tmp_idx * 2+1], heap[tmp_idx]
                tmp_idx *=2

    else:
        heap.append(i)
        idx += 1

        tmp_idx = idx
        while (heap[tmp_idx] > heap[tmp_idx // 2]) and (tmp_idx > 1):
            heap[tmp_idx], heap[tmp_idx // 2] = heap[tmp_idx // 2], heap[tmp_idx]
            tmp_idx = tmp_idx//2

    print(heap)


