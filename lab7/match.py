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
    else:
        return False
