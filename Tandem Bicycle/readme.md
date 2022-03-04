# Name 

Tandem Bicycle

## Type of Question

Greedy Algorithms

## Difficulty

Easy

## Pre-requisites
sort function 


## Description

A tandem bicycle is a bicycle that's operated by two people: person A and person B. Both people pedal the bicycle, but the person that pedals faster dictates the speed of the bicycle. So if person A pedals at a speed of `5`, and person B pedals at a speed of `4`, the tandem bicycle moves at a speed of 5 (i.e., `tandemSpeed = max(speedA, speedB)`).

You're given two lists of positive integers: one that contains the speeds of riders wearing red shirts and one that contains the speeds of riders wearing blue shirts. Each rider is represented by a single positive integer, which is speed that they pedal a tandem bicycle at. Both lists have the same length, meaning that there are as many red-shirt riders as there are blue-shirt riders. Your goal is to pair every rider wearing a red shirt with a rider wearing a blue shirt to operate a tandem bicycle. 

Write a function that returns the maximum possible total speed or the minimum possible total speed of all of the tandem bicycles being ridden based on an input parameter, `fastest`. If `fastest = true`, your function should return the maximum possible total speed; otherwise it should return the minimum total speed. 

"Total Speed" is defined as the sum of the speeds of all the tandem bicycles being ridden. For example, if there are 4 riders (2 red-shirt riders and 2 blue-shirt riders) who have a speed of `1,3,4,5`, and if they're paired on tandem bicycles as follows: `[1,4], [5,3]`, then the total speed of these tandem bicycles is `4 + 5 = 9`

## How I approached the problem

* The first thing you need to do to solve this problem is to sort the array using the sort function. You need to sort the redShirtSpeeds and the blueShirtSpeeds array.

* Next you need to create an if statement for if fastest == false (or true) then create a function that will reverse the array of redShirtSpeeds (alternatively you could've just reverse sorted the redShirtSpeeds). The array will only be reverse if fastest == false or true (please see other code example)

* the reverse array function will contain a value of the start index at 0 and the end index which will be the length of the array - 1:
 
 * In this function we will run a while loop that says while start < end. Then array[start], array[end] = array[end], array[start].
 This pretty much means that given a sorted array for Ex: [1,2,3,4,5] that array[0], array[4] = array[4], array[0]. This would return a value of [5,2,3,4,1].

 * We would then increment the value of the start index by stating start += 1 and decrement the value of the end index by stating end -= 1. There is no need to return the array in this function because it reversing the array in place and not reversing it in a variable. 

* Then you create a variable for totalSpeed = 0 and then iterate through redShirtSpeeds array and going through each index of the array

* Then assign a variable in you for loop to contain the value of the number in redShirtSpeeds index which would be rider 1

* Next you create a variable called rider 2 which will take in the value of the blueShirtsSpeeds array at [len(blueShirtSpeeds) - idx - 1]. 
sb - the reason we use the idx - 1 is because the len(blueShirtSpeeds) is static so it will always equal to the same number but the index changes as we are iterating through the array and the reason we subtract 1 is because indexes are 0 based and do not start at 1.

* Next step is we update the value of totalSpeed to equal the max value of rider1, rider2. For ex: if rider 1 = 3 and rider 2 = 5 then the max number would be 5 so total speed in this example would've been equal to 5.

* We continue increasing the value of totalSpeed based on the max(rider1, rider2). For example let's say in the next idx rider1 = 6 and rider 2 = 3. Then the max of the two riders would be 6 because thats the greater number out of the two and total speed (which in the previous example was updated to 5) would now be equal to 11 (which would be 5 + 6).

* Finally after looping through each index in the redShirtSpeeds array we would return the value of totalSpeed. That's it. 


