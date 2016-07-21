import json
from collections import OrderedDict
# import signal

# from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from sol0 import go


def main(request):
    return HttpResponse('Hello world!')


@csrf_exempt
def max_queens(request):
    # TODO remove this!
    # It's a GET.
    if request.method == 'GET':
        return JsonResponse({'foo': 'bar'})

    # It's a POST.
    # Input format:
    # {
    #     "rows": 8,
    #     "columns": 8,
    #     "max_queens_on_sight": 0,
    #     "initial_queens": [
    #         {"x": 0, "y": 0},
    #         {"x": 1, "y": 2}
    #
    #     ]
    #  }
    data = json.loads(request.body)
    rows_count = data['rows']
    cols_count = data['columns']
    max_queens = data['max_queens_on_sight']
    initial_queens = data['initial_queens']


    queens = []
    for q in initial_queens:
        queens.append((q['x'], q['y']))


    try:
        board = go(max_queens, rows_count, cols_count, queens)
    except Exception as ex:
        print('xxxxxxxx', ex)


    result = []
    for x in xrange(rows_count):
        for y in xrange(cols_count):
            if board[x][y]==1:
               result.append(OrderedDict([('x', x), ('y', y)]))

    #new_queens = solve(rows_count, cols_count, max_queens, initial_queens)
    return JsonResponse({'added_queens': result})


# def build_response(new_queens):
#     lst = [OrderedDict([('x', x[0]), ('y', x[1])]) for x in new_queens]
#     data = {'added_queens': lst}
#     return data


def solve(rows_count, cols_count, max_queens, initial_queens):
    # Do the processing.
    new_queens = [(0,1), (2,3), (4,5)]
    return new_queens