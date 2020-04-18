# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 15:43:24 2020

@author: sridhar
"""

def get_solution(list1,diff):
    list2 = []
    finallist = []
    for i in range (0,len(list1)-1):
        if(i<=0):
            list2.append(list1[i])
               
        if((list1[i+1]-list1[i]) <= diff):
            list2.append(list1[i+1])
        else:
            if(len(list2) > 1):
                finallist.append(list2)
            list2 = []
            list2 = [list1[i+1]]
    if(len(list2)> 1):    
        finallist.append(list2)
        
    print("Given Input",list1)
    print("Given Diffrence", diff)
    print("Output",finallist)
    print("")


list1 = [13, 15, 25, 28, 38]
diff  = 4;
print("Test Input")
get_solution(list1,diff)

list1 = [17, 21, 80, 84, 86, 97, 120]
diff  = 8;
print("Example 1")
get_solution(list1,diff)

list1 = [20, 23, 26, 28, 30, 37, 45, 47, 50, 60, 63, 65]
diff  = 5;
print("Example 2")
get_solution(list1,diff) 

print("For test and Example Output See Above")
print("Enter the Input of your Choice")
n = int(input("Enter the length of the input array : "))
list1 = list(int(num) for num in input("Enter the list numbers separated by space: ").strip().split())[:n]
diff = int(input("Enter the Difference : "))
get_solution(list1,diff)