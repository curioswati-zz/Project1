import sys
from fileinput import *

ip=[]                               #This list is to collect the input L and R as a list for no. of test cases
for line in input():                #Reads stdin'''
    if isfirstline():               #first line of stdin to be no. of test cases
        cases=line[0]
    else:
        i=line.split(" ")           #splitting the line to collect input range(the first no to start with and last to end by) for one test case
        for j in range(0,len(i)):   
            i[j]=int(i[j])          #the input is string so converting them to ints
        ip.append(i)                #appending the inputs as a list to main input list
           
for j in range(0,int(cases)):
    cnt=0                           #to count the numbers that are not to include
    lst=[x for x in range(ip[j][0],ip[j][1]+1)]       #creating a alist with the input range
    for no in lst:        
        no=list(str(no))
        for n in no:                 # n is a single digit of the no     
            c=no.count(n)            # count the occurences of digit n in list no
            if c>1:
                cnt+=1
                break
    print len(lst)-cnt
