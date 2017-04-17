import matplotlib.pyplot as plt
import numpy as np
import math

# *** --------- DATA TABLES -------------- ***
''' ITEMS DATA
   ---------------------------------
   |Class|Weight|Cost|Resale Value |
   ---------------------------------
   .
   .
   .
   .
   .
   N
   
   CONTSTAINTS DATA (INCOMPATIBALITY)
   ---------------------------------
   |ITEM1| ITEM2| ..........|ITEM K|
   ---------------------------------
   .
   .
   .
   .
   .
   T
   
'''


'''
   ---------- QUESTIONS TO CONSIDER ------------
   What affects accuracy of choosing optimal items?
   What affects run time of algorithm with respect to choosing P, M?
   What affects run time of algorithm with respect to choosing Contraints, # of Classes?
   Does class ordering matter? # That is should we randomized our classes when creating the input file
   Hows does the distribution of profit/weight affect the accuracy and performance of algorithm?
   
   
'''
########################### INPUT FILES ##############################################################
'''Creates data for each item:
    N-- Represents the number of items 
    how-- array of length 3 where each entry indicates the way in which we select class, weight, cost & resale value
    P-- weight limit
    M-- money limit
'''
def make_items_data(N,how,P,M):
    data =np.zeros((N,4))
    
    ## ---------------- select ordering of classes ------------ ##
    count_class=0
    if (how[0] == 0): # all differet classes
        for i in range(N):
            data[i,0]=i
    else if(how[0] == 1): # 10 classes only
        divider = N/10
        for i in range(N): 
            data[i,0]=count_class
            if (i % divider == 0)
                divider+= N/10
                count_class+=1
            
    else if(how[0]==2): # create 100 different classes
        divider = N/10
        for i in range(N):
            data[i,0]=count_class
            if (i % divider == 0)
                divider+= N/10
                count_class+=1
    else:
        raise ValueError('Does not reconize class ordering: ',str(how[0]))
    data[:,0]=np.random.shuffle(data[:,0])
            
     # *** -------------- select weights  --------- ***      
            
    if (how[1]==0): #all whole numbers randomly selected from 0 to P
        
    else if (how[1]== 1): # all floats randomly selected from 0 to P
            
    else if (how[1]== 2): # small weights with integers
    
    else if (how[1]== 3): # big weights
        
    
    # *** --------------- select costs & resale value ----------- ***
    
   
    if (how[2]==0): #all whole numbers randomly selected from 0 to P
        
    else if (how[2]== 1): # all floats randomly selected from 0 to P
            
    else if (how[2]== 2): # small costs with whole numbers
    
    else if (how[2]== 3): # big costs with whole numbers
        
        
    return data
           
'''Creates a string for incompatible classes:
    C-- Represents the number of constraints 
    how-- array of length 3 where each entry indicates the way in which we select class, weight, cost & resale value
'''
def make_constraints(C,how):
    
    for i in range(N):
        ####


def input_files(N_items, Contraints,Pounds, Money,how):
    f=open('test1_input.in','w')
    P=str(Pounds) +'\n'
    M=str(Money) +'\n'
    N=str(N_items)+'\n'
    C=str(Constraints)+'\n'
    f.write(P)
    f.write(M)
    f.write(N)
    f.write(C)
    #-------------------- Creating items and adding them to a file --------------------------------#
    
    Data=make_items_data(N_items,how,Pounds,Money) #Nx4 matrix 
    for i in range(N_items):
        item= 'item' + str(i+1)
        line = item +';'+str(Data[i,0])+'; '+str(Data[i,1])+'; '+ str(Data[i,2])+ '; '+ str(Data[i,3])+'\n'
        f.write(line)
        
    #---------- Adding Constraints to file ---------------------------------------------------------#
    
    All= make_constraints(Constraints,how)
    
    f.write(All)
        
    f.close()   
             
              