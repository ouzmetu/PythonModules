def gaussPivot(a,b,tol=1.0e-9):
    n = len(b)

    #Setup Scale Factors
    s = zeros((n), type=Float64)
    for i in  range(n):
        s[i] = max(abs(a[i,:]))

    for k in  range(0, n-1):

        #changing row
        p = int(argmax(abs(a[k:n,k])/s[k:n])) + k
        if abs(a[p,k]) < tol:
            error.err('Matrix is singular')
        if p !=k:
            swap.swapRows(b,k,p)
            swap.swapRows(s,k,p)
            swap.swapRows(a,k,p)

        #Elimination
            for i in  range(k+1,n):
                if a[i,k] !=0.0:
                    lam = a[i,k]/a[k,k]
                    a[i,k+1:n] = a [i,k+1:n] - lam*a[k,k+1:n]
                    b[i] = b[i] - lam*b[k]

    if abs(a[n-1,n-1]) < tol:
        error.err('Matrix is singular')

    #Back Substitution
        for k in range(n-1,-1,-1):
            b[k] = (b[k] - dot(a[k,k+1:n], b[k+1:n]))/a[k,k]
        return b