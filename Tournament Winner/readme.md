# Name 

Tournament Winner

## Type of Question

Array

## Difficulty

Easy

## Description

There's an algorithms tournament taking place in which teams of programmers compete against each other to solve algorithmic problems as fast as possible. Teams compete in a round robin, where each team faces off against all other teams. Only two teams compete against each other at a time, and for each competition, one team is designated the home team, while the other team is the away team. In each competeition there's always one winner and one loser; there are no ties. A team receives 3 points if it wins and 0 points if it loses. The winner of the tournamant is the the team that recieves the most amount of points. 

Given an array of pairs representing the teams that have competed against each other and an array containing the results of each competition, write a function that returns the winner of the Tournament. The input arrays are name `competitions` and `results`, respectively. The `competitions` array has elements in the form of `[homeTeam, awayTeam]`, where each team is a string of at most 30 characters representing the name of the team. The `results` array contains information about the winnner of each corresponding competition in the `competitions` array. Specifically, `results[i]` denotes the winnner of `competitions[i]`, where a `1` in the `results` array means that the home team in the corresponding competition won and a `0` means that the away team won. 

It's guaranteed that exactly one team will win the tournament and that each team will compete against all other teams exactly once. It's also guaranteed that the tournament will always have at least two teams. 

## How I approached the problem

In this problem there is an algorithim competition that only has one winner. Teams compete in pairs and only one team wins each pair competition. At the end of the competition there is only one winner. You are suppose to write a formula where you are taking two input paramaters which are `competitions = array`, and `results= array`. Competitions is an array of the competitors and results is an array of the winners of each competition. If the home team won the results array will say 1 if the away team won the results array will say `0`. The best way to solve this problem is using a hashtable. A hashtable stores indexes and values in it. The first step to completing this problem is creating a global variable stating `HOME_TEAM_WON = 1`. The next step is creating a method called tournament winner where it takes in two paramaters. It takes in the competitions array and the results array. Next step is creating a variable called current best team and assigning it a string value `("")`. Next step is where you are going to use your hashtable. You create a hashtable called scores which will equal `currentbestteam` and the value will be `0`. It will look like this `scores = {currentbestteam:0)`. Then the next step is to iterate over the competitions array using the enumerate method. The enumerate method returns an index and value in the list index when it is iterated. Using the enumerate method we want to return the idx and the competition value in the competitions array. The next step is to set a variable result = results[idx]. idx is the index that we are currently at in the iteration. For example `result = results[idx]` let's say the idx of results is `0` and the value of results in the `0` index is `1` then we have to compare it to the values in the competitions array and see who won that battle. So after creating the result variable we need to assign a value to competition so we say competition = homeTeam, awayTeam. so when the competitions array is inputed we will have the index of each array in the competitions array and the value of each pair in the competions array.  We then create a variable called `winning team = homeTeam if result == HOME_TEAM_WON else awayTeam`. What this pretty much does is it goes through the results array and if it the value is `1` then that means the home team won. If the result is `0` that means the away team won. The value of which team one is stored in the `winningteam` variable. The next step is to create a helper function which will update the scores in the scores dictionary. So you create a function called `updateScores(team, points, scores)`and the function will check if the winning team is in the scores dictionary. If not then it will add it to the dictionary by assigning the value of team that won to equal 0. Then it will increment the value of score by the amount of point won. Ex: `scores[team] += points`. this means in the scores dictionary the winning team value equal the points awarded to them. SB: winning teams receive three points. so in the scores dictionary it will say Ex: `{'C#': 3}` if it was just added. Then the next step is we create an if statement to compare `scores[winningTeam]` and `scores[currentbestTeam]`. if the `scores[winningTeam] > scores[currentbestTeam]` then the `currentbestTeam = winningTeam`. then it continues iterating through the competitions array looking at each pair using the same breakdown. Finally at the end of the for loop it returns the value of the name of the currentbestteam. That's it. 