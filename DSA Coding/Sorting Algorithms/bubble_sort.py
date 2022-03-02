# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 00:20:07 2022

@author: sachi
"""

# Bubble sort in Python

def bubbleSort(array):
    

  for i in range(len(array)):

    
    for j in range(0, len(array) - i - 1):

      
      if array[j] > array[j + 1]:

        
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp


data = []
n=int(input("Number of elemnts in an array:"))
for i in range(0,n):
   l=int(input())
   data.append(l)

bubbleSort(data)

print('Sorted Array is:')
print(data)