def findThreeLargestNumbers(array):
    # Write your code here.
	threeLargest = [None,None,None]
	for num in array:
		updateLargest(threeLargest, num)
	return threeLargest

def updateLargest(threeLargest, num):
	if threeLargest[2] == None or num > threeLargest[2]:
		shiftandUpdate(threeLargest, num, 2)
	elif threeLargest[1] == None or num > threeLargest[1]:
		shiftandUpdate(threeLargest, num, 1)
	elif threeLargest[0] == None or num > threeLargest[0]:
		shiftandUpdate(threeLargest, num, 0)

def shiftandUpdate(array, num, idx):
	for i in range(idx + 1):
		if i == idx:
			array[i] = num
		else:
			array[i] = array[i + 1]


print(findThreeLargestNumbers([1,9,0,15,16,18,25,30,40,50]))