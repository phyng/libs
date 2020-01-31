# coding: utf-8

from __future__ import unicode_literals, absolute_import, print_function

import itertools


def uniqify(sequence, key=None) -> iter:
    """ uniqify

    Return uniqify sequence
    """
    seen = set()
    seen_add = seen.add
    if key is None:
        for x in sequence:
            if x in seen:
                continue
            seen_add(x)
            yield x
    else:
        for x in sequence:
            value = key(x)
            if not (value in seen or seen_add(value)):
                yield value


def chunks(iterable, size=10):
    """ chunks
    """
    it = iter(iterable)
    item = list(itertools.islice(it, size))
    while item:
        yield item
        item = list(itertools.islice(it, size))


def split_to_size(lst, n):
    return (lst[i::n] for i in range(n))
