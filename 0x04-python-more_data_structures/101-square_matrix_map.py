#!/usr/bin/python3
def sqaure_matrix_map(matrix=[]):
    return (list(map(lambda a: list(map(lambda v: v**2, a[:])), matrix)))
