#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 20:35:36 2023
MIT 6.0001 ps0

1. Asks the user to enter a number “x”
2. Asks the user to enter a number “y”
3. Prints out number “x”, raised to the power “y”.
4. Prints out the log (base 2) of “x”. 

@author: hanpeitao
"""
import numpy as np

print('please input x')
x = int(input())
print('plaese input y')
y = int(input())

print('the x power to y is:' + str(x**y))
print('the log of x is:' + str(np.log2(x)))

