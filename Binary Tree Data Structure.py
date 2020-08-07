# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 15:18:20 2020

@author: eric1
"""
   
class Node:
    
    def __init__(self,data):                            
        
        self.left=None
        self.right=None
        self.data=data
        
    def insert(self,data):                                                   # inserting children
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif data >self.data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
                
            
                
        
        else:
            self.data=data
        
    
        
    def Print(self):                                           #prints out the tree
        if self.left:
            self.left.Print()
        print (self.data)
        if self.right:
            self.right.Print()
        
        

root=Node(10)                                                # creates the root
root.insert(12)
root.insert(6)
root.insert(3)
root.insert(1)
root.insert(2)

root.Print()
