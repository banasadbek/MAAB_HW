universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(uni):
	enrollment=[]
	tuition=[]
	for i in uni:
		enrollment.append(i[1])
		tuition.append(i[2])
	return enrollment,tuition

def mean(a):
	return sum(a)/len(a)

def median(a):
	a.sort()
	n=len(a)
	if(n%2):return a[n//2]
	else:return (a[(n-1)//2] + a[n//2])/2

enrollment,tuition = enrollment_stats(universities)
print('''******************************
Total students: {}
Total tuition: $ {}

Student mean: {}
Student median: {}

Tuition mean: $ {}
Tuition median: $ {}
******************************'''.format(	sum(enrollment), 
											sum(tuition), 
											round(mean(enrollment),2), 
											median(enrollment), 
											round(mean(tuition),2),
											median(tuition)))
