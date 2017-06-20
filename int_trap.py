def int_trap(func, sliceWidth, upBound, lowBound):
    integral = 0
    i = 1
    variable = float(lowBound)
    while variable < upBound:
        variable = float(lowBound + i * sliceWidth)
        i += 1
        integral += sliceWidth * (func(variable))
        upBounds = variable + sliceWidth
        if i > 1000 and func(
                variable) < 1.0e-8:
            break
    integral += sliceWidth * ((func(lowBound) + func(upBounds)) / 2)
    return integral