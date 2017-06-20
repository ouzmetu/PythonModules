def swapRows(v,i,j):
    if len(v, getshape()) == 1:
        v[i], v[j] = v[j],v[i]

    else:
        temp = v[i].copy()
        v[i] = v[j]
        v[j] = temp