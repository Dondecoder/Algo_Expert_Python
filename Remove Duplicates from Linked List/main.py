# This is an input class. Do not edit.
# write a function that returns a modified version that includes no duplicates
# test cases = 3-->4--->5--->6--->6----->6--->7-->7 return 3-->4--->5--->6--->7
# first we would need to iterate through linkedlist
# keep track of values in the linked list using a count or something
# if count == itr then itr = self.next

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
	
def removeDuplicatesFromLinkedList(linkedList):
	# Write your code here.
	currentNode = linkedList
	while currentNode is not None:
		nextDistinctNode = currentNode.next
		while nextDistinctNode is not None and nextDistinctNode.value == currentNode.value:
			nextDistinctNode = nextDistinctNode.next
			currentNode.next = nextDistinctNode
			currentNode = nextDistinctNode
		return linkedList
