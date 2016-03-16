from pylab import *
in_fs = open('pulse_data.txt')
#in_ps = open('pulse_data.txt')
vals=[]
n=0
BINS=50
hist=[0]*BINS

for line in in_fs:
    val=float(line)
    # print val
    vals.append(val)
#    n=n+1
#	print n

ovals = list(vals)		
		
#hist
minval=min(vals)
maxval=max(vals)
vspan=maxval-minval
#print vspan
midvalue=(maxval+minval)/2
#print midvalue
for i in vals:
	binid=int(BINS*(i-minval)/vspan)
	if binid==BINS:
		binid = BINS-1
	hist[binid] = hist[binid] + 1
#	print binid

	
#print binid

x=range(0,100000)
vals.sort()
subplot(411)
plot(x,vals,'ro-')
subplot(412)
plot(x,ovals,'go-')
subplot(413)
plot(range(50),hist)
subplot(414)
bar(range(50),hist)
show()