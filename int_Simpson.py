def int_simpson(func, sliceWidth, upBound, lowBound):
    integral = 0
    variable = float(lowBound)
    maxloop = 0
    while variable < upBound:
        integral += func(variable) + (2 * func(variable + sliceWidth))
        maxloop += 1
        if maxloop > 650 and func(
                variable) < 1.0e-8:
            variable += 2 * sliceWidth
            upBounds = variable
            break
        variable += 2 * sliceWidth
    integral = (2 * integral) - func(lowBound) + func(
        upBounds)
    integral = sliceWidth * integral / 3
    return integral