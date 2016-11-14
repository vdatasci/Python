def countdown(x):
    if x<=0:
        print 'Finished!'
    else:
        print x
        countdown(x-1)
