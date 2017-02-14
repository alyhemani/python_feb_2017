str = 'If monkeys like bananas, then I must be a monkey!'
print str.find('monkey')
print str.replace('monkey', 'alligator')

x = [2,54,-2,7,12,98]
print max(x)
print min(x)

y = ["hello",2,54,-2,7,12,98,"world"]
z = []
first = y[:1] 
last = y[7:]
z.append(first)
z.append(last)
print z

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
newlist = []
for i in x[:]:
	if i < 0:
		newlist.append(i)
		x.remove(i)
x.insert(0,newlist)
print x
