def bisection(f, a, b, TOL=0.001, NMAX=100):
    n=1
    while n<=NMAX:
        c = (a+b)/2.0
        print "a=%s\tb=%s\tc=%s\tf(c)=%s"%(a,b,c,f(c))
        if f(c)==0 or (b-a)/2.0 < TOL:
            return c
        else:
            n = n+1
            if f(c)*f(a) > 0:
                a=c
            else:
                b=c
    return False