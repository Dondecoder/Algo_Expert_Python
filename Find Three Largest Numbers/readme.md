# Name 

Find Three Largest Numbers

## Type of Question

Searching Algorithms

## Difficulty

Easy

## Pre-requisites

Helper Functions 

Arrays

## Description

Write a function that takes in an aray of at least three integers and, without sorting the input array, return a sorted array of the three largest intgers in the input array. 

The function should return duplicate integers if necessary; for example, it should return `[10,10,12]` for an input array of `[10,5,9,10,12]`. 

## How I approached the problem

### Step One

* Create a array that would store the value of the threeLargest numbers. Assign a None value to each place from index `0` - `2`. 
Sb - The reason it is better to use a non value in this case is because if you assign a value of `0` you may get an input array that has negative numbers and that might mess up your algorithim 

    ```python
    threeLargest = [None, None, None]
    ```

### Step Two 

* Iterate through the input array and create a helper function that will update the threeLargest array for each value in the input array and after iterating through the array the findThreeLargestNumbers function will return the threeLargest array

    ```python
    for num in array:
        updateLargest(threeLargest, num)
    return threeLargest
    ```

### Step Three 

* Create a helper function that will update the threeLargest array at each index starting at the last index first

    ```python
    def updateLargest(threeLargest, num):
        if threeLargest[2] == None or num > threeLargest[2]:
            shiftandUpdate(threeLargest, num, 2)
        elif threeLargest[1] == None or num > threeLargest[1]:
            shiftandUpdate(threeLargest, num, 1)
        elif threeLargest[0] == None or num > threeLargest[0]:
            shiftandUpdate(threeLargest, num, 0)
    ```

* To give further explanation this helper function updates the threeLargest array starting at index `2` it states that if index[`2`] == None or num > threeLargest[`2`] you should run a function that shifts the number from right to left in the threeLargest array. As the numbers grow in value we will check each index of the threeLargest array and see if the current number is greater than the number at that given index. 

### Step Four

* Create a function that will shift the numbers for you as the values in the input array increase. If the values are greater than numbers currently in the threeLargest array than the we will put that number toward the end of the array and take a number or value off the array by shifting numbers from right to left.

    ```python
    def shiftandUpdate(array, num, idx):
        for i in range(idx + 1):
            if i == idx:
                array[i] = num
		    else:
                array[i] = array[i + 1]
    ```

SB - Let's say we were to use an array of values `[1,6,9,2]`. The first thing we would do would be to create a ThreeLargest variable to store `3` values in an array. Then we would create an update array function that will update each index of the ThreeLargest array based on the value of the number in the input array. Then based on the value and the index we will shift numbers off the array and add numbers to the threeLargest array. If in doubt run the debugger to refresh. 