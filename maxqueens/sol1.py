
class Cell(object):
    __slots__ = ['queen', 'count', 'max_queens', 'closed']

    def __init__(self, queen=False, count=0, max_queens=0):
        self.queen = queen
        self.count = count
        self.max_queens = max_queens
        self.closed = False

    def increment(self):
        self.count += 1

    def closeit(self):
        self.count = self.max_queens + 1
        self.closed = True

    def __str__(self):
        return '%s%s' % ('Q' if self.queen else '-', self.count)


class Solution(object):
    def __init__(self, max_queens, cols_count, rows_count, initial_queens):
        self.max_queens = max_queens
        self.cols_count = cols_count
        self.rows_count = rows_count
        self.initial_queens = initial_queens
        self.matrix = [[-1] * cols_count for _ in xrange(rows_count)]
        self.init_matrix()
        self.fill_new_queens()


    def init_matrix(self):
        for row_ix in xrange(self.rows_count):
            for col_ix in xrange(self.cols_count):
                self.matrix[row_ix][col_ix] = Cell(False, 0, self.max_queens)

        for row_ix, col_ix in self.initial_queens:
            self.add_queen(row_ix, col_ix)


    def add_queen(self, row_ix, col_ix):
        cell = self.matrix[row_ix][col_ix]
        cell.queen = True
        cell.increment()

        if cell.count > self.max_queens:
            # Col, row and diag are full (set them to self.max_queens+1).
            self.set_full_adjacents(row_ix, col_ix)
            # set row, col, diags to max_queens
        else:
            # Increment row, col, diags.
            self.increment_adjacents(row_ix, col_ix)
        self._print()
        print('')


    def increment_adjacents(self, row_ix, col_ix):
        for runner in xrange(1, max(rows_count, cols_count)):
            # Increment right (row and diag).
            right_col = col_ix + runner
            if right_col < self.cols_count:
                self.matrix[row_ix][right_col].increment()
                if row_ix + runner < self.rows_count:
                    self.matrix[row_ix + runner][right_col].increment()
                if row_ix - runner >= 0:
                    self.matrix[row_ix - runner][right_col].increment()

            # Increment left (row and diag).
            left_col = col_ix - runner
            if left_col >= 0:
                self.matrix[row_ix][left_col].increment()
                if row_ix + runner < self.rows_count:
                    self.matrix[row_ix + runner][left_col].increment()
                if row_ix - runner >= 0:
                    self.matrix[row_ix - runner][left_col].increment()

            # Increment col.
            if row_ix + runner < self.rows_count:
                self.matrix[row_ix + runner][col_ix].increment()
            if row_ix - runner >= 0:
                self.matrix[row_ix - runner][col_ix].increment()


    def set_full_adjacents(self, row_ix, col_ix):
        def set_close(row_ix, col_ix):
            c = self.matrix[row_ix][col_ix]
            if c.queen and not c.closed:
                to_close.append((row_ix, col_ix))
            c.closeit()


        to_close = [(row_ix, col_ix)]

        while len(to_close):
            r_ix, c_ix = to_close.pop()
            for runner in xrange(1, max(rows_count, cols_count)):
                # Set close right (row and diag).
                right_col = c_ix + runner
                if right_col < self.cols_count:
                    set_close(r_ix, right_col)
                    if r_ix + runner < self.rows_count:
                        set_close(r_ix + runner, right_col)
                    if r_ix - runner >= 0:
                        set_close(r_ix - runner, right_col)

                # Set close left (row and diag).
                left_col = c_ix - runner
                if left_col >= 0:
                    set_close(r_ix, left_col)
                    if r_ix + runner < self.rows_count:
                        set_close(r_ix + runner, left_col)
                    if r_ix - runner >= 0:
                        set_close(r_ix - runner, left_col)

                # Set close col.
                if r_ix + runner < self.rows_count:
                    set_close(r_ix + runner, c_ix)
                if r_ix - runner >= 0:
                    set_close(r_ix - runner, c_ix)


    def fill_new_queens(self):
        # c = self.matrix[0][0]
        # if c.count <= max_queens:
        #     self.add_queen(0, 0)
        # return

        for row_ix in xrange(rows_count):
            for col_ix in xrange(cols_count):
                c = self.matrix[row_ix][col_ix]
                if c.count <= max_queens:
                    self.add_queen(row_ix, col_ix)


    def _print(self):
        for r in self.matrix:
            for c in r:
                print('{}'.format(c)),
            print('')


if __name__ == '__main__':
    max_queens = 2  # TOD 1 is 0!!
    cols_count = 4
    rows_count = 4
    initial_queens = ((1, 0), (3, 1))
    # initial_queens = ((1, 1),)
    solution = Solution(max_queens, cols_count, rows_count, initial_queens)
    solution._print()











































def go():
    max_queens = 0
    cols_count = 4
    rows_count = 4
    initial_queens = ((1, 0), (3, 1))
    #matrix = init_matrix(rows_count, cols_count, initial_queens)



    return matrix




    for c in initial_queens:
        matrix[c[0]][c[1]] = 'Q'
        increment_row(matrix, c[0], cols_count)
        increment_col(matrix, c[1], rows_count)
        increment_diagonals(matrix, c[0], c[1], rows_count, cols_count)

    for row_ix in xrange(rows_count):
        for col_ix in xrange(cols_count):
            # print(matrix[row_ix][col_ix])
            # if val <= max_queens:
            #    keep track of queen pos
            #    update col
            #    update row
            #    update diagonals
            #    set cell val to max_queens + 1

            # if matrix[row_ix][col_ix] == max_queens:
            #     new_queens.append((row_ix, col_ix))
            #     increment_row(matrix, row_ix, cols_count, max_queens+1)
            #     increment_col(matrix, col_ix, rows_count, max_queens+1)
            #     increment_diagonals(matrix, row_ix, col_ix, rows_count, cols_count, max_queens+1)
            #     matrix[row_ix][col_ix] = max_queens + 1

            if matrix[row_ix][col_ix] <= max_queens:
                # new_queens.append((row_ix, col_ix))
                matrix[row_ix][col_ix] = 'Q'
                increment_row(matrix, row_ix, cols_count)
                increment_col(matrix, col_ix, rows_count)
                increment_diagonals(matrix, row_ix, col_ix, rows_count, cols_count)


    print('\n\n\nEND')
    return matrix, new_queens



def _increment(matrix, row_ix, col_ix):
    if not matrix[row_ix][col_ix] == 'Q':
        matrix[row_ix][col_ix] += 1


def increment_row(matrix, row_ix, cols_count):
    for c in xrange(cols_count):
        _increment(matrix, row_ix, c)


def increment_col(matrix, col_ix, rows_count):
    for r in xrange(rows_count):
        _increment(matrix, r, col_ix)


def increment_diagonals(matrix, row_ix, col_ix, rows_count, cols_count):
    runner = 0
    for r in xrange(row_ix+1, rows_count):
        runner += 1
        if col_ix + runner < cols_count:
            _increment(matrix, r, col_ix+runner)
        if col_ix - runner >= 0:
            _increment(matrix, r, col_ix-runner)

    runner = 0
    for r in xrange(row_ix-1, -1, -1):
        runner += 1
        if col_ix + runner < cols_count:
            _increment(matrix, r, col_ix+runner)
        if col_ix - runner >= 0:
            _increment(matrix, r, col_ix-runner)


def _print_matrix(m):
    for r in m:
        for e in r:
            print(' {} '.format(e)),
        print('')


# if __name__ == '__main__':
#     matrix = go()
#     _print_matrix(matrix)