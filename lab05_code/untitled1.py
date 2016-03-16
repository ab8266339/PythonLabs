from pylab import *
in_fs = open('pulse_data.txt')
#in_ps = open('pulse_data.txt')
ts=[]
vs=[]
x=[]
y=[]
bs=[]
vals=[]
n=0
BINS=100
Value=0.333
for line in in_fs:
    val=float(line)
    # print val
    vals.append(val)
    n=n+1
minval=min(vals)
maxval=max(vals)
vspan=maxval-minval
print vspan
value=(value-minval)/vspan
binid=int(BINS*(vals-minval)/vspan)
print value,binid
x=range(0,100000)
vals.sort()
# subplot(211)
# plot(x,vals,'go-')