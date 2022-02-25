# Name 

Product Sum

## Type of Question

Recursion

## Difficulty

Easy

## Pre-requisites
* Recursion

* type function

## Description

Write a function that takes in a "special" array and returns its product sum. A "special" array is a non-empty array that contains either integers or other "special" arrays. The product sum of a "special" array is the sum of its elements, where "special" arrays inside it are summed themselves and then multiplied by their level of depth. 

The depth of a "special" array is how far nested it is. For instance, the depth of `[]` is `1`; the depth of the inner array in `[[]]` is `2`; the depth of the innermost array in `[[[]]]` is `3`.

Therefore, the product sum of `[x,y]` is `x + y`; the product sum of `[x,[y,z]]` is `x + 2 * (y + 2)`; the product sum of `[x,[y,[z]]]` is `x + 2 * (y + 3z)`.

## How I approached the problem

* Comment the code with special paramaters dictated in the problem

* Create a product sum function that takes in an array and a multiplier = 1

* Within the function you can create a sum variable equal to 0 

* Then you iterate through the array and create an if statement stating if type(element) == list:
then you make a recursive call to the function that will update the sum variable by the value of the recursive call to the productSum function

```python
for element in array:
    if type(element) == list:
        sum += productSum(element, multiplier + 1)
```

* Next you create an else clause that will update the sum variable by adding the element to the current value of the sum variable.

```python
    else:
        sum += element
```

* Finally the function will return the `sum * multiplier`