def gcd(q, p):
    """
    Parameters
    ----------
    q : int
        Has the first given value
    p : int
        Has the second given value

    Return
    ------
    gcd(p, q%p) : function
        recursive return where q%p is the module that we give
    p : int
        return p when the module of q % p is 0
    """
    if p > q:
        return gcd(p, q)
    if q % p == 0:
        return p
    return gcd(p, q % p)


print(gcd(12, 8))
