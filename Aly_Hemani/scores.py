print "Scores and Grades"
for count in range(0,10):
	import random
	random_num = random.random()*100
	if (random_num > 90):
		grade = "A"
	elif (90 > random_num > 80):
		grade = "B"
	elif (80 > random_num > 70):
		grade = "C"
	elif (70 > random_num > 60):
		grade = "D"
	elif (random_num < 60):
		grade = "F"
	print "score %d; Your grade is %s" %(random_num, grade)
print "End of program. Goodbye"

