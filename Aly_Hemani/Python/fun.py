for count in range (1, 2001):
	if count%2 == 1:
		print 'Number is {}'.format(count) +'. This is an odd number.'
	else: 
		print 'Number is {}'.format(count) +'.This is an even number'


a = [2,4,10,16]
b = 5
a = [x * b for x in a]
print a