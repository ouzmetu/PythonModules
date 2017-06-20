def trapezoid(f,a,b,Iold,k):
    if k == 1:Inew = (f(a) + f(b))*(b - a)/2.0
    else:
    n = 2**(k -2 ) # Number of new points
    h = (b - a)/n # Spacing of new points
    x = a + h/2.0 # Coord. of 1st new point
    sum = 0.0
    for i in range(n):
    sum = sum + f(x)
    x = x + h
    Inew = (Iold + h*sum)/2.0


###  # below module could be useful for integral calculation

def compute_integral_w_trapezoid(u,Nmax=20):
    Iold = 0.
    for k in range(1,Nmax+1):
        Inew = trapezoid(int_part_g,0.0,1./u,Iold,k)
        if (k>1) and (abs(Inew - Iold) < 1.e-6) : break
        Iold = Inew
    return Inew
###