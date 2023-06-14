### 1.1
def count_stair_ways(n):
    if n < 0 :
        return 0
    elif n <= 1:
        return 1
    else:
        return count_stair_ways(n-1) + count_stair_ways(n-2)

###1.2
def count_k(n, k):
    """
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    if n < 0:
        return 0
    elif n <= 1:
        return 1
    else:
        result = 0
        for i in range(1, k+1):
            result += count_k(n-i, k)
        return result

###2.2
def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [x * s[x] for x in range(len(s)) if x % 2 == 0]
    

###2.3
def max_product(s):
    """Return the maximum product that can be formed using non-consecutive
    elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if len(s) == 0:
        return 1
    elif len(s) == 1:
        return s[0]
    elif len(s) == 2:
        return max(s[0], s[1])
    else:
        return max(s[0] * max_product(s[2:]), max_product(s[1:]))

