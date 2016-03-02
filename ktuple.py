import math

def generateItems(str1, str2):
	items = list(set(str1))
	items.extend(list(set(str2))) 
	return list(set(items))

def generateKTuple(items, k):
	ktuple = []
	recurseGenerateKTuple("", k, 0, ktuple, items)
	return ktuple

def recurseGenerateKTuple(str, k, kcur, ktuple, items):
	if kcur == k:
		ktuple.append(str)
	else:
		for item in items:
			recurseGenerateKTuple(str + item, k, kcur + 1, ktuple, items)
	return

def generateDistanceMatrix(str1, str2, ktuple):
	distanceMatrix = []
	for eachTuple in ktuple:
		distanceMatrix.append(abs(str1.count(eachTuple)-str2.count(eachTuple)))

	return distanceMatrix

def generateDistance(distanceMatrix):
	distanceMatrixSqr = [eachNum**2 for eachNum in distanceMatrix]
	distance = math.sqrt(sum(distanceMatrixSqr))

	return distance

def ktuple_string(str1, str2, k):
	items = generateItems(str1, str2)
	ktuple = generateKTuple(items, k)
	distanceMatrix = generateDistanceMatrix(str1, str2, ktuple)
	print(distanceMatrix)
	distance = generateDistance(distanceMatrix)

	return distance

# test
# distance = ktuple_string("abc", "abcde", 3)
# print(distance)

