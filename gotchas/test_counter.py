"""
sum(c.values())                 # total of all counts
c.most_common()[:-n-1:-1]       # n least common elements
c.clear()                       # reset all counts
+c                              # remove zero and negative counts
list(c)                         # list unique elements
set(c)                          # convert to a set
dict(c)                         # convert to a regular dictionary
c.items()                       # convert to a list of (elem, cnt) pairs
Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
"""

from collections import Counter


def test_ints_counter():
    """
    take elements from a list
    create a map with counter foreach distinct element
        select element, count(*) from list group by element

    >>> Counter([3, 4, 3, 5, 3, 4])
    Counter({3: 3, 4: 2, 5: 1})
    """
    assert Counter([3, 4, 3, 5, 3, 4])[3] == 3


def test_most_common_words():
    """
    >>> # Find the ten most common words in Hamlet
    >>> # open('hamlet.txt').read().lower()
    >>> hamlet = "Indeed, indeed, sirs, but this troubles me.".lower()
    >>> import re
    >>> from collections import Counter
    >>> words = re.findall(r'\w+', hamlet)
    >>> Counter(words).most_common(1)
    [('indeed', 2)]
    """
