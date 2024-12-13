import books


def match(seq, pattern):
    """
    Returns whether given sequence matches the given pattern
    """
    if not pattern:
        return not seq
    elif pattern[0] == '--':
        if match(seq, pattern[1:]):
            return True
        elif not seq:
            return False
        else:
            return match(seq[1:], pattern)
    elif not seq:
        return False
    elif pattern[0] == '&':
        return match(seq[1:], pattern[1:])
    elif seq[0] == pattern[0]:
        return match(seq[1:], pattern[1:])
    elif isinstance(seq[0], list) and isinstance(pattern[0], list):
        return match(seq[0], pattern[0]) and match(seq[1:], pattern[1:])
    else:
        return False


def search(pattern, seq):
    """Returns matching element to pattern in seq"""
    res = []
    for elem in seq:
        if match(elem, pattern):
            res.append(elem)
    return res


a = [['a', ['b', ['c']]], ['a', 'b']]
b = ['--', ['år', 2042], '--']
c = [['författare', ['&', 'glenn', '&']], ['titel', ['--', 'science', '--']], ['år', '&']]
d = ['--', ['titel', ['&', '&']], '--']
#print(search(c, books.db))



