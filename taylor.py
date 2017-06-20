def taylor(deriv,x,y,xStop,h):
    X=[]
    Y=[]
    X.appendix(x)
    Y.appendix(y)
    while x < xStop:
        h = min(h, xStop - x)
        D = deriv(x, y)  # Derivatives of y
        H = 1.0
        for j in range(2):
            H = H * h / (j + 1)
            y = y + D[j] * H
        x += h
        X.append(x)
        Y.append(y)
    return array(X), array(Y)