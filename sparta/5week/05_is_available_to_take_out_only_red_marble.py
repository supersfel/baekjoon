from collections import deque
from copy import deepcopy

map = [
    ["#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", ".", ".", "#", "B", "#"],
    ["#", ".", "#", "#", "#", "#", "#"],
    ["#", ".", ".", "R", ".", ".", "#"],
    ["#", "#", "#", "#", "#", ".", "#"],
    ["#", "O", ".", ".", ".", ".", "#"],
    ["#", "#", "#", "#", "#", "#", "#"]

]

dr = [0,1,0,-1]
dc = [-1,0,1,0]




def is_available_to_take_out_only_red_marble(game_map):


    d = 0
    count = 0
    for i in range(len(game_map)):
        if "R" in game_map[i]:
            red_r = i
            red_c = game_map[i].index("R")
        if "B" in game_map[i]:
            blue_r = i
            blue_c = game_map[i].index("B")

    queue = deque()
    queue.append((red_r, red_c, blue_r, blue_c,game_map))
    
    full_count = 0
    for x in range(10):
        full_count += 4**x


    while count <=full_count:
        red_r, red_c, blue_r, blue_c, present_game_map = queue.popleft()
        for j in range(4):
            new_game_map = deepcopy(present_game_map)
            # print('present_game_map')
            #
            # for x in range(len(present_game_map)):
            #     print(present_game_map[x])
            # print('----------------------')

            for i in range(len(game_map)):
                if "R" in present_game_map[i]:
                    red_r = i
                    red_c = present_game_map[i].index("R")
                if "B" in present_game_map[i]:
                    blue_r = i
                    blue_c = present_game_map[i].index("B")


            new_red_r = red_r + dr[j]
            new_red_c = red_c + dc[j]
            new_blue_r = blue_r + dr[j]
            new_blue_c = blue_c + dc[j]


            if present_game_map[new_red_r][new_red_c] == "O":
                return True
            elif present_game_map[new_red_r][new_red_c] == "#":
                new_red_r, new_red_c = red_r, red_c
            elif present_game_map[new_red_r][new_red_c] == "B" and present_game_map[new_red_r +dr[j]][new_red_c +dc[j]] != ".":
                new_red_r, new_red_c = red_r, red_c


            if present_game_map[new_blue_r][new_blue_c] == "O":
                new_blue_r, new_blue_c = blue_r, blue_c
            elif present_game_map[new_blue_r][new_blue_c] == "#":
                new_blue_r, new_blue_c = blue_r, blue_c


            elif present_game_map[new_blue_r][new_blue_c] == "R" and present_game_map[new_blue_r+dr[j]][new_blue_c+dc[j]] != ".":
                new_blue_r, new_blue_c = blue_r, blue_c


            new_game_map[red_r][red_c] ,new_game_map[new_red_r][new_red_c] = new_game_map[new_red_r][new_red_c],new_game_map[red_r][red_c]
            new_game_map[blue_r][blue_c], new_game_map[new_blue_r][new_blue_c] = new_game_map[new_blue_r][new_blue_c],new_game_map[blue_r][blue_c]


            if new_game_map[new_blue_r][new_blue_c] != "O" :
                queue.append((new_red_r,new_red_c,new_blue_r,new_blue_c,new_game_map))


            # print('new_game_map')
            # for x in range(len(present_game_map)):
            #     print(new_game_map[x])
            # print('----------------------')
        count +=1


    return False


print(is_available_to_take_out_only_red_marble(map))  # True 를 반환해야 합니다