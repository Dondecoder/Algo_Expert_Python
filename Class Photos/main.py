# Students wear two colors
# red and blue
# arrange students in two rows
# All students wearing red shirts must be in the same row
# All students wearing blue shirts must be in the same row
# Each student in back row must be taller than studen directly in front of them in
# front row.
# Each class has at least two students
# redShirtHeights = [1,3,5,7,9] blueshirtHeights = [2,4,6,8,10]

def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
	red_sort = sorted(redShirtHeights)
	blue_sort = sorted(blueShirtHeights)
	
	last_row= "RED" if red_sort[0] > blue_sort[0] else "BLUE"
	
	for idx in range(len(red_sort)):
		red_value = red_sort[idx]
		blue_value = blue_sort[idx]
		
		if last_row == "RED":
			if red_value <= blue_value:
				return False
		if last_row == "BLUE":
			if blue_value <= red_value:
				return False
	return True
