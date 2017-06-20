def printSoln(X,Y,freq):

    def printHead(n):
        print  "\n x"
        for i in range(n):
            print "        y[",i,"] ",
        print

    def printLine(x,y,n):
        print "%13.4e"% x,
        for i in range(n):
            print " %13.4e" % y[i],
        print