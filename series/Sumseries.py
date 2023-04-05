def sum_series(n,first=0,second=1):
    if n ==0:
        return first
    elif n ==1:
        return second
    else:
        return sum_series(n-1,first,second) + sum_series(n-2,first,second)

    