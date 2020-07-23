# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 13:00:09 2020

for more details on Hanoi Tower see https://en.wikipedia.org/wiki/Tower_of_Hanoi

@author: eric1
"""


# INPUT SIZE (exponential problem, keep small)


size=4

## Algorithm Steps: ## Step 1: Move the smallest disk from its current peg to the next peg in
##                             clockwise direction.
###                 ##Step 2: Make the only move possible that does not involve the smallest disk





# Initialise Towers at the start, stack_1 has the tower
# Desired is a copy of the complete stack
stack_1=[]
stack_2=[]
stack_3=[]
desired=[]
stacks=[stack_1,stack_2,stack_3]

for i in range(1,size):
    stack_1.append(0)
    desired.append(0)
    
    
for i in range(1,size):
    stack_1.append(size-i)
    stack_2.append(0)
    stack_3.append(0)


for i in range(1,size):
    desired.append(size-i)
    

print (stacks)                 # prints 3 stacks config at the beginning
    
    


def step1():
    
    var=0
    for i in range(3):
        #print (i)
        if 1 in stacks[i]:
            #print (stacks[i])
            if i==2:
                stacks[0].append(stacks[i].pop())
                
                var=0
            
            else:
                stacks[i+1].append(stacks[i].pop())
                
                var=i+1
            break
    #print ("step 1:")
    #print(stacks)
    print ("\n")
    return (var)
            

def step2(x):
    for i in range(3):
        if i==x:
            continue
            
        for j in range(3):
            #print (i , j)
            if j==x:
                continue
            if j==i:
                continue
            k1=stacks[i][-1]
            k2=stacks[j][-1]
            
            if k1==0:
                stacks[i].append(stacks[j].pop())
                print (stacks)
                break
            if k2==0:
                stacks[j].append(stacks[i].pop())
                print (stacks)
                break
            
            if k2<k1:
                stacks[i].append(stacks[j].pop())
                print (stacks)
                break
            else:
                stacks[j].append(stacks[i].pop())
                print (stacks)
                break
            
        break
    
def master():   
    
    while True:
        taken=step1()
        if stack_2 ==desired:
            print ("FINISHED")
            print (stacks)
            break
        if stack_3==desired:
            print ("FINISHED")
            print (stacks)
            break
        else:
                       
            step2(taken)
            
            
            
     
master()    # call master function to run
    
