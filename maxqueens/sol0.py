import copy
import time


# def handler(signum, frame):
#     raise Exception("Timeout")


DURATION = 1.8
#LOOPS = 500000

def go(max_queens, rows_count, cols_count, initial_queens):
    #max_queens = 5
    #cols_count = 80
    #rows_count = 80
    #initial_queens = ((0, 0),)  # ((1, 0), (3, 1))

    # signal.signal(signal.SIGALRM, handler)
    # signal.setitimer(signal.ITIMER_REAL, .5)

    if rows_count == cols_count == 1 and not initial_queens:
        return [(1,1),]

    board = [[0] * cols_count for _ in xrange(rows_count)]
    return solve(board, initial_queens, max_queens, rows_count, cols_count)


def predict_max_queens(max_queens, rows_count, cols_count):
    if max_queens == 0:
        if rows_count > 3 and rows_count <= cols_count:
            return rows_count
        if cols_count > 3 and cols_count <= rows_count:
            return cols_count
        if rows_count == 1 or cols_count == 1:
            return 1
        if (cols_count >= 3 and rows_count > 3) or (
                cols_count > 3 and rows_count >= 3):
            return 3
        if (cols_count >= 2 and rows_count > 2) or (
                cols_count > 2 and rows_count >= 2):
            return 2
    return rows_count * cols_count


def solve(board, initial_queens, view_queens, rows_count, cols_count):

    global DURATION
    sum_ = rows_count + cols_count
    if sum_ > 300:
        DURATION = 1.7
    if sum_ > 2000:
        DURATION = 1.65

    start_time = time.time()

    queens_found = 0
    queens_found_max = 0
    row_ix = 0
    col_ix = 0
    loops = 0
    predicted_max_queens = predict_max_queens(view_queens, rows_count,
                                              cols_count)
    # print('predicted_max_queens', predicted_max_queens)
    for c in initial_queens:
        board[c[0]][c[1]] = -1
        queens_found += 1

    queens_found_max = queens_found
    board_max = copy.deepcopy(board)

    duration = time.time() - start_time

    while duration < DURATION and queens_found < predicted_max_queens  and ( #and loops < LOOPS
            queens_found >= 0 or loops == 0):
        loops += 1
        if queens_found > queens_found_max:
            queens_found_max = queens_found
            board_max = copy.deepcopy(board)
            # print('NEW MAX QUEENS', queens_found)
        if board[row_ix][col_ix] == 0 and isValid(board, row_ix, col_ix,
                                                  view_queens, rows_count,
                                                  cols_count, 2):
            board[row_ix][col_ix] = 1
            queens_found += 1
        if row_ix >= rows_count - 1 and col_ix >= cols_count - 1:
            while board[row_ix][col_ix] < 1 and col_ix >= 0 and row_ix >= 0:
                col_ix -= 1
                if col_ix < 0:
                    row_ix -= 1
                    col_ix = cols_count - 1
            if col_ix >= 0 and row_ix >= 0:
                board[row_ix][col_ix] = 0
                queens_found -= 1
                if row_ix >= rows_count - 1 and col_ix >= cols_count - 1:
                    while board[row_ix][
                        col_ix] < 1 and col_ix >= 0 and row_ix >= 0:
                        col_ix -= 1
                        if col_ix < 0:
                            row_ix -= 1
                            col_ix = cols_count - 1
                    if col_ix >= 0 and row_ix >= 0:
                        board[row_ix][col_ix] = 0
                        queens_found -= 1

        col_ix += 1
        if col_ix >= cols_count:
            col_ix = 0
            row_ix += 1
        duration = time.time() - start_time

    if queens_found > queens_found_max:
        queens_found_max = queens_found
        board_max = copy.deepcopy(board)
    #     print('NEW MAX QUEENS', queens_found)
    # print('loops', loops)
    # print('queens_left', queens_found)
    # print('queens_found_max', queens_found_max)
    return board_max



def isValid(board, row_ix, col_ix, view_queens, rows_count, cols_count,
            counter):
    if counter <= 0:
        return True
    if view_queens < 0:
        return False
    queens = 0
    for y in xrange(cols_count):
        if board[row_ix][y] != 0 and y != col_ix:
            if isValid(board, row_ix, y, view_queens - 1, rows_count,
                       cols_count, counter - 1):
                queens += 1
            else:
                return False
    if queens > view_queens:
        return False
    for x in xrange(rows_count):
        if board[x][col_ix] != 0 and x != row_ix:
            if isValid(board, x, col_ix, view_queens - 1, rows_count,
                       cols_count, counter - 1):
                queens += 1
            else:
                return False
    if queens > view_queens:
        return False
    # top left
    x = row_ix - 1
    y = col_ix - 1
    while x >= 0 and y >= 0:
        if board[x][y] != 0:
            if isValid(board, x, y, view_queens - 1, rows_count, cols_count,
                       counter - 1):
                queens += 1
            else:
                return False
        x -= 1
        y -= 1
    # top right
    x = row_ix - 1
    y = col_ix + 1
    if queens > view_queens:
        return False
    while x >= 0 and y < cols_count:
        if board[x][y] != 0:
            if isValid(board, x, y, view_queens - 1, rows_count, cols_count,
                       counter - 1):
                queens += 1
            else:
                return False
        x -= 1
        y += 1
    if queens > view_queens:
        return False
    # bottum left
    x = row_ix + 1
    y = col_ix - 1
    while x < rows_count and y >= 0:
        if board[x][y] != 0:
            if isValid(board, x, y, view_queens - 1, rows_count, cols_count,
                       counter - 1):
                queens += 1
            else:
                return False
        x += 1
        y -= 1
    # bottum right
    x = row_ix + 1
    y = col_ix + 1
    if queens > view_queens:
        return False
    while x < rows_count and y < cols_count:
        if board[x][y] != 0:
            if isValid(board, x, y, view_queens - 1, rows_count, cols_count,
                       counter - 1):
                queens += 1
            else:
                return False
        x += 1
        y += 1
    if queens > view_queens:
        return False

    return True


# def _print_matrix(m):
#     for r in m:
#         for e in r:
#             print(' {} '.format(e)),
#         print('')


# def _print_matrix1(m, rows_count, cols_count):
#     for row_ix in xrange(rows_count):
#         for col_ix in xrange(cols_count):
#             if (row_ix, col_ix) in a:
#                 ina = '.'
#             else:
#                 ina = ' '
#             if (row_ix, col_ix) in u:
#                 inu = '*'
#             else:
#                 inu = ' '
#             print(' {}'.format(m[row_ix][col_ix])) + ina + inu,
#         print('')
#     print('')


#
# if __name__ == '__main__':
#     # Register the signal function handler
#     # signal.signal(signal.SIGALRM, handler)
#     # signal.setitimer(signal.ITIMER_REAL, .2)
#
#
#     max_queens = 0
#     cols_count = 8
#     rows_count = 8
#     initial_queens = ((0, 0),)  # ((1, 0), (3, 1))
#
#
#     board = go(max_queens, rows_count, cols_count, initial_queens)
#     _print_matrix(board)
# # print(new_queens)
