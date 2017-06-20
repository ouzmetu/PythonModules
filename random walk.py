import pylab, random

nsteps = input('number of steps in walk->')
nwalks = input('number of random walks ->')
seed = input('random numner seed ->')
random.seed(seed)
steps = range(nsteps)
xrms = [0.0] * nsteps

for i in range(nwalks):
    x = [0]*nsteps
    for n in  steps[1:]:
        x[n] = x[n-1]+random.choice([-1, +1])
        xrms[n] += (x[n]**2-xrms[n])/(i+1)
    pylab.plot(steps, x, 'o-')
for n in steps:
    xrms[n] = xrms[n]**0.5


pylab.title('random')
pylab.xlabel('sda')
pylab.ylabel('dsadas')
pylab.grid()
pylab.figure()
pylab.title('rootmeansquare')
pylab.plot(steps, xrms, '.')
pylab.plot(steps, [n**0.5 for n in steps], '-')
pylab.xlabel('step number')
pylab.ylabel('root number')
pylab.grid()
pylab.show()
