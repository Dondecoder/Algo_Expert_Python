# Name 

Binary Search

## Type of Question

Searching Algorithms

## Difficulty

Easy

## Description

Write a function that takes in a sorted array of integers as well as a target integer. The function should use the Binary Search algorithm to determine if the target integer is contained in the array and should return its index if it is, otherwise `-1`.

## Pre-requisites

Binary Search

* With Binary Search we first need a sorted array or an array that can be sorted. 

* The next step that you do is divide the array in half. Then you compare the value that is at the half way point of the array to the target number. If the value is greater than the  target number then you can completely eliminate the right half of the array and proceed with cutting the left half of the array in half (this is in cases where the list is in acending order). 

* If the value is less than the the target number then you can complettly eliminate the left half of the array and proceed with cutting the right half of the array in half (this is in cases where the list is in ascending order)

* If the middle value of the right half of the array is greater than the targer then you move to the left. If it's less than the target you move to the right. 

* If the middle value of the left half of the array is greater than the targer then you move to the left. If it's less than the target you move to the right.

* You should continue this process of cutting the array until you reach your target number.

Recursion

* Calling the same function again until a base paramater is met. Meaning calling the function until a piece of your code breaks the function call. 

## How I approached the problem

For this problem I created was a function that takes in an array and a target:

```python
def binarySearch(array, target):
    pass
```

The second step was to find a way to cut this initial input array in half to traverse it to find the target number. So I created a helperfunction

```python
def binarySearchHelper(array, target, left, right):
    pass
```

* This function is suppose to take the initial array and target and also have a left and right value. The left value to start will be 0 and the right value will be the `len(array) - 1`

The third step was to create a mid variable that would add up the index value of the left variable and the right variable and then return the integer value of that number:

```python
mid = (left + right) // 2
```

The fourth step was to create a while loop so the function continues traversing the array until a condition is met and it will only stop until a base condition is met.

```python
while left <= right:
        if array[mid] == target:
            return mid
        elif array[mid] < target:
		    return binarySearchHelper(array, target, mid + 1, right)
        elif array[mid] > target:
		    return binarySearchHelper(array, target, left, mid - 1)
```

* This function will continue traversing the array as long as the left value <= to the right value and if the middle value of the array is equal to the target number it will return that number. If not then if the the middle number in the array is less than the target then it will call the binarySearchHelper function again except the left value will be mid index +  1. If the array middle value is greater than the target value it will call the binarySearchHelper function except the right index value will be mid -1. It will continue calling the function until the base case is reached which is `if array[mid] == target: return mid`


If the target number is not in the array then it will `return -1`

The last step is to return the results of the binarySearchHelper in the initial binarySearch function. Your final code should look like this:

```python
def binarySearch(array, target):
    # Write your code here.
    return binarySearchHelper(array, target, 0, len(array) -1)
    
	
	
	
	
def binarySearchHelper(array, target, left, right):
	mid = (left + right) // 2
	while left <= right:
        if array[mid] == target:
            return mid
        elif array[mid] < target:
		    return binarySearchHelper(array, target, mid + 1, right)
        elif array[mid] > target:
		    return binarySearchHelper(array, target, left, mid - 1)
    return -1
```
