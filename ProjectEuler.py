#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  pe.py
# Created       :  Mon 27 Apr 2015 19:01:22
# Last Modified :  Sat 30 May 2015 23:34:56
# Maintainer    :  sharlatan, <ssharlatanus@gmail.com>
# Title         :  PROJECT EULER FUNCTIONS
# License       :  Same as Python (GPL)
# Credits       :  https://projecteuler.net
#
# -=:[ DESCRIPTION ]:=-
# This file contains functions which I used for solving Project Euler's
# problems.
# num is alway a integer number given as argument to any of functions.
# <END OF DESCRIPTION>---------------------------------------------------------


def fnls():
    """ Return a list of used functions with short description. """
    function_list = {
        "isp(num)"    : "Check num for primality.",
        "ps(num)"     : "Yield prime sieve up to num.",
        "divs(num)"   : "Yield list of proper divisor of num.",
        "ds(num)"     : "Recursively return digits sum of num.",
        "dfs(num)"    : "Return factorised digits sum of num.",
        "dsfs(num)"   : "Return digit sum of factorised digit sum.",
        "pclrow(num)" : "Yield the n'th row of Pascal triangle.",
        "trgn(num)"   : "Yield a list of integer triangular numbers up to num.",
        "ttrn(n)"     : "Yield a list of int tetrahedral nums up to n's pos.",
        "sqrn(n)"     : "Yield a list of int square nums up to n's pos.",
        "pntn(num)"   : "Yield a list of int pentagoanl nums up to n's pos."
                    }
    for key in function_list:
        print key,"\t:", function_list[key]
# <END  OF  DESCRIPTION>-------------------------------------------------------


import math
import itertools


# -=:[ Prime numbers ]:=-
def isp(num):
    """ Is prime?: check num for primality. """
    if num == 1:
        return False
    elif num < 4:
        return True  # 2 and 3 are primes
    elif num % 2 == 0:
        return False
    elif num < 9:  # already excluded 4, 6 and 8.
        return True
    elif num % 3 == 0:
        return False
    else:
        r = int(math.sqrt(num))  # rounded r so that r*r <= num
        f = 5
        while f <= r:
            if num % f == 0:
                return False
            elif num % (f + 2) == 0:
                return False
            f += 6
    return True


def ps(n):
    """ Prime sieve: generate prime sieve up to n's position. """
    i = 2
    while i < n:
        if isp(i):
            yield i
        i += 1
# <END OF PRIME NUMBERS>--------------------------------------------------------


# -=:[ Divisors ]:=-
def divr(ran, num):
    """ Divisor range: generate a list of number in ran dividable by num. """
    r = 2
    while r < ran:
        if r % num == 0:
            yield r
        r += 1


def divs(num):
    """ Yield unsorted list of proper divisor of num. """
    for d in xrange(1, int(math.sqrt(num))):
        if num % d == 0:
            yield d
            yield num // d


def divp(num):
    ''' Prime divisors: generate range of prime divi for num. '''
    for d in xrange(2, int(math.sqrt(num))):
        if isp(d) and num % d:
            yield d
# <END OF  DIVISORS>------------------------------------------------------------




def ds(num):
    """ Recursively return digits sum of num. """
    if num < 10:
        return num
    return num % 10 + ds(num // 10)


def dfs(num):
    """ Return factorised digits sum of num. """
    if num < 10:
        return math.factorial(num)
    return math.factorial(num % 10) + dfs(num // 10)


def dsfs(num):
    """ Return digit sum of factorised digit sum. """
    return ds(dfs(num))


def pclrow(n):
    """ Yield the n'th row of Pascal triangle. """
    pos = 1
    yield pos
    for k in xrange(1, n):
        pos = pos * (n+1 - k) / k
        yield pos
    yield 1


# -=:[ Figurate numbers ]:=-
def trgn(n, only_one=None):
    """ Triangular numbers:  generate a list of ingeter trgn  up to num. """
    if only_one == "one":
        yield n * (n + 1) / 2
    else:
        for tr in xrange(0, n+1):
            yield tr*(tr+1)/2


def sqrn(n, only_one=None):
    ''' Square number[s]: generate list of sqrn if not given "one". ''' 
    if only_one == "one":
        yield n**2
    else:
        for sq in xrange(0, n+1):
            yield sq**2


def pntn(n, only_one=None):
    ''' Pentagonal number[s]: yeild list if not "one".'''
    if only_one == "one":
        yield (3 * n**2 - n) / 2
    else:
        for pen in xrange(0, num+1):
            yield (3 * pen**2 - pen) / 2


def hexn(n, only_one=None):
    ''' Hexagonal number: generated up to n's position. '''
    if only_one == "one":
        yield n * (2*n - 1)
    else:
        for h in xrange(0, n+1):
            yield h * (2*h - 1)


def hepn(n, only_one=None):
    ''' Heptagoanl number: generated up to n's position. '''
    if only_one == "one":
        yield  n * (5*n - 3) / 2
    else:
        for hep in xrange(0, n+1):
            yield n * (5*n - 3) / 2


def octn(n, only_one=None):
    ''' Octagoanl number: generated up to n's position. '''
    if only_one == "one":
        yield  n * (3*n + 2)
    else:
        for o in xrange(0, n+1):
            yield o * (3*o + 2)


def ttrn(n):
    """ Yield a list of integer tetrahedral numbers up to n's position. """
    for n in xrange(0, n+1):
        yield (n*(n + 1) * (n + 2)) / 6
# <END OF FIGURATE NUBERS>-----------------------------------------------------


# -=:[ Reference ]:=-
# Carl Friedrich Gauss
# Euler's theory of partions
# OEIS : A000217

# -=:[ Links ]:=-
# https://en.wikipedia.org/wiki/Triangular_number
