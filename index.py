sumOfSquares=0
squareOfSums=0
counter=0
for i in range(101):
	sumOfSquares=sumOfSquares+i*i
for i in range(101):
	squareOfSums=squareOfSums+i
squareOfSums=squareOfSums * squareOfSums
print(squareOfSums - sumOfSquares)
