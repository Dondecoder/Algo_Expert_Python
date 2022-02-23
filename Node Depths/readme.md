# Name 
### Node Depths

## Type of Question
### Binary Tree

## Diffictulty
### Easy

## Description
#### The distance between a node in Binary Tree and the tree's root is called the node's depth. Write a function that takes in a Binary Tree and returns the sum of its nodes' depths. Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can either be BinaryTree nodes themselves or None/ null.

## How I approached the problem
#### There are two ways to do this iterativily and recursively. The iterative approach creates a stack and updates the stack as it goes through the binary search tree. The recursive approach starts from the root of the tree and traverses down the tree completely to the left side until it trigers the base case. To understand the recursive approach you need to understand that the formula or function will continue traversing until it hits its base case and from there it will begin to traverse upward to the root node. In this case in order to get the right output you have to understand with recursion it has to completly complete the left side before it can start the right side. only after it reaches the base case on the left side can it begin traversing upward and work on the right side.  To fully understand this problem you have to understand that each node in the tree is put through the recursive function once the base case is hit. The recursive function will return a value and that is how much is associated with that specific node.  
