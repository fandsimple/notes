#!/usr/bin/python
# -*- coding: utf-8 -*-



import selectors
import pdb




def p():
    yield 1
    yield 2
    yield 3

print(next(p()))
print(next(p()))
