current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]




def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    able = sum([len(list(filter(lambda x: x == 0, i))) for i in room_map])  # 0 갯수
    done = []  # 위치
    result = 0  # 결과

    x = len(room_map[0]) - 1
    y = len(room_map) - 1

    for _ in range(able):
        print("=======================")
        print("r : {} | c : {} | d : {}".format(r, c, d))
        # 왼쪽방향 탐색, direct = 이동방향
        direct = d  # 0 1 2 3
        back = False
        # 벽돌 & 백상태
        if back and room_map[r][c]:
            return len(done)

        if (r, c) not in done:
            done.append((r, c))

        while (1):
            # 북방향 동
            if d == 0:
                # 벽과 데이터 없으면
                if not room_map[r][c - 1] and (r, c - 1) not in done:
                    c -= 1
                    d += 1
                    break
                elif back:
                    r += 1
                    break
            # 동방향 남
            elif d == 1:
                if not room_map[r + 1][c] and (r + 1, c) not in done:
                    r += 1
                    d += 1
                    break
                elif back:
                    c += 1
                    break
            # 남방향 서
            elif d == 2:
                if not room_map[r][c + 1] and (r, c + 1) not in done:
                    c += 1
                    d += 1
                    break
                elif back:
                    r -= 1
                    break
            # 서방향 북
            elif d == 3:
                if not room_map[r - 1][c] and (r - 1, c) not in done:
                    r -= 1
                    d = 0
                    break
                elif back:
                    c -= 1
                    break
            # 방향 전환 및 사방 막힘?
            d += 1
            d %= 4
            if d == direct:
                back = True

    return len(done)


# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))