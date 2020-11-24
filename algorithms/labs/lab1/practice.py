

def triangle(n, m):
    if n == 1:
        pass
    else:
        triangle(n-2, m+1)
        print(' ' * (m + 1) + ((n - 2) * '*'))


triangle(13, 0)

