import copy


def go():
    max_queens = 0
    cols_count = 8
    rows_count = 8
    matrix = [[0] * cols_count for _ in xrange(rows_count)]
    init_matrix = [[0] * cols_count for _ in xrange(rows_count)]
    initial_queens_input = [(0, 3)]
    new_queens = []
    all_queens = copy.deepcopy(initial_queens_input)
    number_of_queens = 1  # trick
    #    print('MAX queens',max_queens)
    initial_queens = copy.deepcopy(initial_queens_input)

##    while number_of_queens > 0 and number_of_queens < 8:


    #	    print('init')
    #	    print(all_queens)
    upd_queens = []
    #            print('DEBUG1',initial_queens)
    for c in initial_queens:
        increment_row(all_queens, matrix, c[0], c[1], cols_count, 1, 1)
        increment_col(all_queens, matrix, c[0], c[1], rows_count, 1, 1)
        increment_diagonals(all_queens, matrix, c[0], c[1], rows_count,
                            cols_count, 1, 1)
        matrix[c[0]][c[1]] += 1
    update_queens(upd_queens, all_queens, matrix, max_queens, cols_count,
                  rows_count)

    for row_ix in xrange(rows_count):
        for col_ix in xrange(cols_count):
            if matrix[row_ix][col_ix] <= max_queens:
                if not (row_ix, col_ix) in all_queens:
                    new_queens.append((row_ix, col_ix))
                    all_queens.append((row_ix, col_ix))
                    number_of_queens += 1
                    increment_row(all_queens, matrix, row_ix, col_ix,
                                  cols_count, 1, 1)
                    increment_col(all_queens, matrix, row_ix, col_ix,
                                  rows_count, 1, 1)
                    increment_diagonals(all_queens, matrix, row_ix, col_ix,
                                        rows_count, cols_count, 1, 1)
                    matrix[row_ix][col_ix] += 1
                    # print('Adding queen',row_ix, col_ix)
                    # _print_matrix1(upd_queens,all_queens,matrix,rows_count,cols_count)
                    # _print_matrix(matrix)
                    update_queens(upd_queens, all_queens, matrix,
                                  max_queens, cols_count, rows_count)

    print('Number of Queens', number_of_queens)
    _print_matrix1(upd_queens, all_queens, matrix, rows_count, cols_count)

    if False:
    # if number_of_queens < 8:
        x, y = new_queens.pop()
        matrix = [[0] * cols_count for _ in xrange(rows_count)]
        init_matrix = [[0] * cols_count for _ in xrange(rows_count)]
        matrix[x][y] = max_queens + 1
        number_of_queens -= 1
        #                print('DEBUG1',all_queens)
        all_queens = copy.deepcopy(initial_queens_input + new_queens)
        initial_queens = copy.deepcopy(all_queens)
        # print('DEBUG2',all_queens)

    _print_matrix1(upd_queens, all_queens, matrix, rows_count, cols_count)
    print('\nEND')
    return matrix, new_queens


def update_queens(upd_queens, all_queens, matrix, max_queens, cols_count,
                  rows_count):
    # print(all_queens)
    for c in all_queens:
        if matrix[c[0]][c[1]] > max_queens and not (c[0], c[1]) in upd_queens:
            increment_row(all_queens, matrix, c[0], c[1], cols_count,
                          max_queens + 1, 0)
            increment_col(all_queens, matrix, c[0], c[1], rows_count,
                          max_queens + 1, 0)
            increment_diagonals(all_queens, matrix, c[0], c[1], rows_count,
                                cols_count, max_queens + 1, 0)
            upd_queens.append((c[0], c[1]))


# print('Update queens', c[0], c[1])
#    	   _print_matrix1(upd_queens,all_queens,matrix,rows_count,cols_count)

def increment_row(all_queens, matrix, row_ix, col_ix, cols_count, increment,
                  no_queen):
    for c in xrange(cols_count):
        if c <> col_ix:
            if (row_ix, c) in all_queens:
                if no_queen == 1:
                    matrix[row_ix][c] += 1
            else:
                matrix[row_ix][c] += increment


def increment_col(all_queens, matrix, row_ix, col_ix, rows_count, increment,
                  no_queen):
    for r in xrange(rows_count):
        if r <> row_ix:
            if (r, col_ix) in all_queens:
                if no_queen == 1:
                    matrix[r][col_ix] += 1
            else:
                matrix[r][col_ix] += increment


def increment_diagonals(all_queens, matrix, row_ix, col_ix, rows_count,
                        cols_count, increment, no_queen):
    runner = 0
    for r in xrange(row_ix + 1, rows_count):
        runner += 1
        if col_ix + runner < cols_count:
            if (r, col_ix + runner) in all_queens:
                if no_queen == 1:
                    matrix[r][col_ix + runner] += 1
            else:
                matrix[r][col_ix + runner] += increment
        if col_ix - runner >= 0:
            if (r, col_ix - runner) in all_queens:
                if no_queen == 1:
                    matrix[r][col_ix - runner] += 1
            else:
                matrix[r][col_ix - runner] += increment
    runner = 0
    for r in xrange(row_ix - 1, -1, -1):
        runner += 1
        if col_ix + runner < cols_count:
            if (r, col_ix + runner) in all_queens:
                if no_queen == 1:
                    matrix[r][col_ix + runner] += 1
            else:
                matrix[r][col_ix + runner] += increment
        if col_ix - runner >= 0:
            if (r, col_ix - runner) in all_queens:
                if no_queen == 1:
                    matrix[r][col_ix - runner] += 1
            else:
                matrix[r][col_ix - runner] += increment


def _print_matrix(m):
    for r in m:
        for e in r:
            print(' {} '.format(e)),
        print('')


def _print_matrix1(u, a, m, rows_count, cols_count):
    for row_ix in xrange(rows_count):
        for col_ix in xrange(cols_count):
            if (row_ix, col_ix) in a:
                ina = '.'
            else:
                ina = ' '
            if (row_ix, col_ix) in u:
                inu = '*'
            else:
                inu = ' '
            print(' {}'.format(m[row_ix][col_ix])) + ina + inu,
        print('')
    print('')


if __name__ == '__main__':
    matrix, new_queens = go()
    _print_matrix(matrix)
    print(new_queens)
