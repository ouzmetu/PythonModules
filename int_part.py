def int_part_g(x):
    if x==0 :
        v = 0.
    else :
        v = ( x**4 * exp(x) ) / ( ( exp(x) - 1 )**2 )
    return v