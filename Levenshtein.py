'''Levenshtein Distance'''

def lev(a,b):
    i = len(a)
    j = len(b)

    # first three cases
    if i == 0:
        return j
    elif j == 0:
        return i

    diff = 0
    if a[0] != b[0]:
        diff = 1
    return min( [ lev(a[1:i], b) + 1, lev(a, b[1:j]) + 1, lev(a[1:i], b[1:j]) + diff] )

print(lev("kitten", "sitting"))
print(lev("beer", "mama"))
print(lev("Android","iOS"))
print(lev("ying","yang"))

