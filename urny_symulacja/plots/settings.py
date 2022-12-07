from math import sqrt
from numpy import log as ln


def n(n):
    return n


def sqrtn(n):
    return sqrt(n)


def lnn(n):
    return ln(n)


def lnn_lnlnn(n):
    return (ln(n)) / ln(ln(n))


def lnlnn(n):
    return ln(ln(n))


def nlnn(n):
    return n * ln(n)


def nn(n):
    return n * n


def nlnlnn(n):
    return n * ln(ln(n))


DATA = {
    'B': [n, sqrtn],
    'U': [n],
    'L': [lnn, lnn_lnlnn, lnlnn],
    'C': [n, nlnn, nn],
    'D': [n, nlnn, nn],
    'DC': [n, nlnn, nlnlnn]
}