# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
# product sum of a "special" array is the sum of its elements, where values of special
# arrays inside it are summed 

def productSum(array, multiplier =1):
    sum = 0
    for element in array:
        if type(element) == list:
            sum += productSum(element, multiplier + 1)
        else:
            sum += element
    return sum * multiplier

print(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))