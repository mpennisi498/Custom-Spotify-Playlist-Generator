import math


# Sources and Citations
# https://www.geeksforgeeks.org/max-heap-in-python/
# https://www.geeksforgeeks.org/python-dictionary/
# https://www.geeksforgeeks.org/floor-ceil-function-python/
# Discussion 7 - Exam 1 Review slides
# Anthony Zurita


class MaxHeap:

    def __init__(self):
        self.heapsize = 0
        self.heap = []


    def parent(self, position):
        return math.floor((position-1) / 2)

    def leftChild(self, position):
        return (2 * position) + 1

    def rightChild(self, position):
        return (2 * position) + 2

    def compareNodes(self, child, parent):
        return self.heap[child]['popularity'] - self.heap[parent]['popularity']
    
    def returnSize(self):
        return self.heapsize

    def heapifyUp(self):

        child = len(self.heap) - 1

        while child > 0:
            parent = self.parent(child)

            if self.compareNodes(child, parent) <= 0:
                break
            # swapping nodes occurs if the nodes priorities/popularity values are different if they are the same, or
            # it is smaller no need for a swap
            self.heap[child], self.heap[parent] = (self.heap[parent], self.heap[child])
            child = parent

    def insertNode(self, popularity, ID, artistName, genre, explicit):
        # a node will be a dictionary holding important info
        node = {'popularity': popularity, 'ID': ID, 'artistName': artistName, 'genre': genre, 'explicit': explicit}    

        # if nothing in the heap then insert at index one and increment size
        if self.heapsize == 0:
            self.heap.append(node)
            self.heapsize += 1
            return
        # otherwise insert at the end of the array and call heapify up to retain max heap properties
        self.heap.append(node)
        self.heapsize += 1

        self.heapifyUp()

    def heapifyDown(self, parent):

        # very first pass maxIndex will be 0 after recursive calls it will change and also
        # change left and right child too
        leftChild = self.leftChild(parent)
        rightChild = self.rightChild(parent)

        maxIndex = parent

        if rightChild < self.heapsize and self.heap[rightChild]['popularity'] > self.heap[maxIndex]['popularity']:
            maxIndex = rightChild

        if leftChild < self.heapsize and self.heap[leftChild]['popularity'] > self.heap[maxIndex]['popularity']:
            maxIndex = leftChild

        if maxIndex != parent:
            self.heap[maxIndex], self.heap[parent] = (self.heap[parent], self.heap[maxIndex])
            self.heapifyDown(maxIndex)

    def extractMax(self):

        if self.heapsize == 0:
            return
        popped = self.heap[0]
        self.heap[0] = self.heap[self.heapsize - 1]
        # assigns the last element in the list to be the first element in the list (first step of deletion)
        # delete last element since not needed anymore
        # decrement size since an item was popped off
        del self.heap[self.heapsize - 1]
        self.heapsize -= 1
        # after deleting the root and replacing it with the last node, heapify down to keep max heap properties
        # putting 0 as the input because it will start heapify down from the root which is index 0
        self.heapifyDown(0)

        return popped


