import re
"""
This module encodes a string using Soundex, as described by
http://en.wikipedia.org/w/index.php?title=Soundex&oldid=466065377

Only strings with the letters A-Z and of length >= 2 are supported.
"""

invalid_re = re.compile("[AEHIOUWY]|[^A-Z]")
charsubs = {'B': '1', 'F': '1', 'P': '1', 'V': '1',
            'C': '2', 'G': '2', 'J': '2', 'K': '2',
            'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
            'D': '3', 'T': '3', 'L': '4', 'M': '5',
            'N': '5', 'R': '6'}


def normalize(s):
    """ Returns a copy of s without invalid chars and repeated letters. """
    # remove invalid chars
    first = s[0].upper()
    s = re.sub(invalid_re, "", s.upper()[1:])

    # remove repeated chars
    char = None
    s_clean = first
    for c in s:
        if char != c:
            s_clean += c
        char = c

    return s_clean


def soundex(s):
    """ Encode a string using Soundex.
    Takes a string and returns its Soundex representation.
    >>> soundex("ashcraft")
    'A261'
    >>> soundex("ashcroft")
    'A261'
    >>> soundex("rubin")
    'R150'
    >>> soundex("robert")
    'R163'
    >>> soundex("rupert")
    'R163'
    >>> soundex("euler")
    'E460'
    >>> soundex("ellery")
    'E460'
    >>> soundex("gauss")
    'G200'
    >>> soundex("ghosh")
    'G200'
    >>> soundex("hilbert")
    'H416'
    >>> soundex("heilbronn")
    'H416'
    >>> soundex("knuth")
    'K530'
    >>> soundex("kant")
    'K530'
    >>> soundex("lloyd")
    'L430'
    >>> soundex("ladd")
    'L300'
    >>> soundex("lukasiewicz")
    'L200'
    """
    if len(s) < 2:
        return None

    s = normalize(s)
    last = None
    enc = s[0]
    for c in s[1:]:
        if len(enc) == 4:
            break

        if charsubs[c] != last:
            enc += charsubs[c]
        last = charsubs[c]

    while len(enc) < 4:
        enc += '0'

    return enc


if __name__ == "__main__":
    import doctest
    doctest.testmod()
