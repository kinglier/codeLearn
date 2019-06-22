#2019.6.20 lixs
# A test about DP operation


def Root(x,a):
    if len(a) == 1:
        return a[0] -x

    resultSeleLeft = (a[0] - x) 
