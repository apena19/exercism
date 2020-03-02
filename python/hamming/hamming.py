def distance(strand_a, strand_b):
    if len(strand_a) == len(strand_b):
        dif = 0
        i = 0
        for c in strand_a:
            if c != strand_b[i]:
                dif += 1
            i += 1
        return dif
    else:
        raise ValueError(".+")
