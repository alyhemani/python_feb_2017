print "Starting the Program..."

x = 0
y = 0
for count in range(0,100000):
	import random
	prob = round(random.random())
	if (prob == 0.0):
		outcome = "heads"
		x = x+1
	elif (prob == 1.0):
		outcome = "tails"
		y = y+1
	print "Throwing a coin ... It's a {} Got {} head(s) so far and {} tail(s) so far".format(outcome, x, y)
print "End of Program. Run again"