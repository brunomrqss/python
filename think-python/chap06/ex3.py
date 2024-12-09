def ackermann(m, n):
    if m == 0:
        return n+1 

    if m > 0 and n == 0:
        n = 1
        return m-1, n
    
    if m > 0 and n > 0:
        return m-1, (m, n-1)
    
ackermann(5, 5)