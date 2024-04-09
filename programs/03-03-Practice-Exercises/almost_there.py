
def almost_there_n(n,k):
    if k <= 0:
        raise Exception("K must be greater than 1")
    return min([abs(n - k * 100) for k in range(1,k+1)]) <= 10
