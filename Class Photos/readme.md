# Name 

Class Photos

## Type of Question

Greedy Algorithms

## Diffictulty

Easy

## Description

It's photo day at the local school, and you're the photographer assigned to take class photos. The class that you'll be photographing has an even number of students, and all these students are wearing red or blue shirts. In fact, exactly half of the class is wearing red shirts, and the other half is wearing blue shirts. You're responsible for arranging the students in two rows before taking the photo. Each row should contain the same number of the students and should adhere to the following guidelines:

All students wearing 

## How I approached the problem

For this problem the first thing that you need to do is extract the main point from the problem. The main point in this problem is that there is a class and half of the classmates are wearing red shirts and the other half are wearing blue shirts.  They are scheduled to take class pictures. There are paramaters to the class photos, here they are: 

All students wearing red shirts must be in the same row 
All students wearing blue shirts must be in the same row
Each student in the back row must be taller than students directly in front of them in the front row
The best way to approach this problem is iterably.
The first step you do is sort the two arrays you are given for the heights of redshirt students and the heights of blueshirt students. 

Create a variable to store the sorted arrays for me I created a red_sort and blue_sort variable. Then you need to create a variable that stores a value for either RED or BLUE depending on the instructions. I created a last_row variable that states:

last_row = "RED" if red_sort[0] > blue_sort[0] else "BLUE".. What this variable pretty much states that if the first index value of red shirted students is greater than the value of the first index of blue shirted student we know that the last row should be red because all red students need to be in the same row. The next step that I did was iterate through the red_sort array and assign variables to values in the red_sort array and the blue_sort array. Now the next step is to check the last_row. One thing we know is if the last_row is RED then no value in red can be less than or equal to blue. If that is the case then they do not qualify for a class photo. Same thing goes for Blue if the last row is equal to Blue then no value of red can be greater than blue and no value of blue can be less than red if that's the case then they do not qualify for a class photo. Other than that you can return True for any other situation. And there you go that is the solution.   
