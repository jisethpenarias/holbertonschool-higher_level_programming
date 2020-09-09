#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    d_a = tuple_a + (0, 0)
    d_b = tuple_b + (0, 0)
  return d_a[0] + d_b[0], d_a[1] + d_b[1]
