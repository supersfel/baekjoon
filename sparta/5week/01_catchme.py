from collections import deque

c = 11
b = 2
queue = deque()

def catch_me(cony_loc, brown_loc):
    # 구현해보세요!
    time = 0
    queue = deque()
    queue.append((brown_loc,0))
    visited = [{} for _ in range(201)]
    print(queue)

    while cony_loc < 200000:
        cony_loc += time
        print(cony_loc)
        if time in visited[cony_loc]:
            print(cony_loc)
            return time

        for i in range(0,len(queue)):
            current_position, current_time = queue.popleft()

            new_time = current_time+1
            new_position = current_position - 1
            if 0 <= new_position <= 200000:
                queue.append((new_position,new_time))
                visited[new_position][new_time] = True
            new_position = current_position + 1
            if 0 <= new_position <= 200000:
                queue.append((new_position, new_time))
                visited[new_position][new_time] = True
            new_position = current_position * 2
            if 0 <= new_position <= 200000:
                queue.append((new_position, new_time))
                visited[new_position][new_time] = True

        print(visited[25])
        time +=1





print(catch_me(c, b))  # 5가 나와야 합니다!