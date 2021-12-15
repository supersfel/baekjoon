sudoku = [list(map(int,input().split())) for _ in range(9)]

def f(sudoku,col,row):


    for line in sudoku:  #탈출검사
        if 0 in line:
            break
    else:
        for x in range(9):
            print(' '.join(map(str, sudoku[x])))
        quit(0) #1개만 출력

    col_lst = [sudoku[x][row] for x in range(9)]
    c , r = col//3 * 3 ,row//3 *3
    piece_sudoku = [] #3*3스도구 조각
    for i in range(3):
        for j in range(3):
            piece_sudoku.append(sudoku[c+i][r+j])

    for num in range(1,10):
        new_col,new_row=0,0;
        if num in sudoku[col]:
            continue
        elif num in col_lst:
            continue
        elif num in piece_sudoku:
            continue

        oldnum = sudoku[col][row]
        sudoku[col][row] = num
        for i in range(col,9):
            if 0 in sudoku[i]:
                new_col = i
                new_row = sudoku[i].index(0)
                break

        f(sudoku,new_col,new_row)
        sudoku[col][row] = oldnum

    return 0


for i in range(9):
    if 0 in sudoku[i]:
        col = i
        row = sudoku[i].index(0)
        break

f(sudoku,col,row)