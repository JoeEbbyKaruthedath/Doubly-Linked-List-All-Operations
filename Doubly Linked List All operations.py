# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 18:42:25 2022

@author: joeeb
"""

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    #Creation of doubly linked list
    def creationDLL(self, nodeValue):
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
    
    def insertionDLL(self, nodeValue, position):
        if self.head == None:
            print("The DLL does not exist")
        else:
            newNode = Node(nodeValue)
            if position == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            
            elif position == 1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
                
            else:
                tempNode = self.head
                index = 0
                while index < position - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                newNode.next = nextNode
                newNode.prev = tempNode
                tempNode.next = newNode
                nextNode.prev = newNode
    #Traverse the DLL           
    def traverseDLL(self):
        if self.head == None:
            print("The DLL is Empty")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
    
    #Reverse traverse the DLL
    def revtraverseDLL(self):
       if self.head is None:
           print("The DLL is empty")
       else:
           tempNode = self.tail
           while tempNode:
               print(tempNode.value)
               tempNode = tempNode.prev
     
        #Search for an element          
    def searchDLL(self, target):
        if self.head is None:
            print("The DLL is empty")
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == target:
                    print("The target exists in the node")
                    break
                elif tempNode.next == None:
                    print("The value does not exist in the node")
                    break
                else:
                    tempNode = tempNode.next
    
    #Delete a particular node at a location
    def deletionDLL(self, location):
        if self.head is None:
            print("The DLL is empty")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            if location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index += 1
                    break
                nextNode = tempNode.next
                tempNode.next = nextNode.next
                nextNode.next.prev = tempNode
    
    #Delete the entire list
    def deleteDLL(self):
        if self.head is None:
            print("The DLL does not exist")
        else:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print("The DLL is delelted")

                    
                    
        
                
            
                
                
doublyLL = DoublyLinkedList()

doublyLL.creationDLL(5)        
print([node.value for node in doublyLL])        

doublyLL.insertionDLL(0, 0)
doublyLL.insertionDLL(2, 1)
doublyLL.insertionDLL(6, 2)
print([node.value for node in doublyLL]) 

doublyLL.searchDLL(6)
doublyLL.searchDLL(9)

doublyLL.deletionDLL(1)
print([node.value for node in doublyLL])

doublyLL.deleteDLL()
print([node.value for node in doublyLL]) 
