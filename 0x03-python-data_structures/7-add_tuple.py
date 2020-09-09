#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result = [0, 0]

    for idx, elementResult in enumerate(result):
        if len(tuple_b) == len(tuple_a):
            result[idx] = tuple_a[idx] + tuple_b[idx]
        elif len(tuple_b) + 1 == len(tuple_a):
            if idx == 0:
                result[idx] = tuple_a[idx] + tuple_b[0]
            else:
                result[idx] = tuple_a[idx] + elementResult
        else:
            result[idx] = elementResult + tuple_a[idx]

    tupleResult = tuple(result)
    return tupleResult
