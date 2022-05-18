W, H, X, Y, P = map(int,input().split())
radius = H // 2                 # 반지름 길이
width = W + X                   # 직사각형 가로 길이
height = H + Y                  # 직사각형 세로 길이
center1 = [X, Y+ radius]        # 반원 중심좌표 1
center2 = [X + W, Y + radius]   # 반원 중심좌표 2

# print(center2)
count = 0
for i in range(P):
    x, y = map(int,input().split())        # 기준 x, y 좌표

    if X <= x and x <= width and Y <= y and y <= height:  # 직사각형 범위 안
        count += 1
    elif ((x - center1[0]) ** 2) + ((y - center1[1]) ** 2) <= (radius ** 2) and x <= X:   # 왼쪽 반원 범위 안
        count += 1
    elif ((x - center2[0]) ** 2) + ((y - center2[1]) ** 2) <= (radius ** 2) and width <= x:  # 오른쪽 반원 범위 안
        count += 1


print(count)