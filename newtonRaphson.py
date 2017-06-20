def newtonRaphson(f,df,a,b,tol=1.0e-9):
    import error
    fa = f(a)
    if fa == 0.0: return a
    fb = f(b)
    if fb == 0.0: return b
    if fa * fb > 0.0: error.err(’Root is not bracket’)
    x = 0.5 * (a + b)
    for i in range(30):
        fx = f(x)
    if abs(fx) < tol: return x
    if fa * fx < 0.0:
        b = x
    else:
        a = x;
    fa = fx
    dfx = df(x)
    try:
        dx = -fx / dfx
    except ZeroDivisionError:
        dx = b - a
    x = x + dx
    if (b - x) * (x - a) < 0.0:
        dx = 0.5 * (b - a)
    x = a + dx
    if abs(dx) < tol * max(abs(b), 1.0): return x
    print ’Too many iterations in Newton - Raphson’
