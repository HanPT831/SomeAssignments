#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 20:57:01 2023
MIT 6.0001 ps1 part A: house hunting
@author: hanpeitao
"""
months = 0
portion_down_payment = 0.25
current_savings = 0
r = 0.04
print('Enter your annual salary:')
annual_salary = float(input())
monthly_salary = annual_salary/12
print('Enter the percent of your salary to save, as a decimal:')
portion_saved = float(input())
print('Enter the cost of your dream home: ')
total_cost = float(input())
down_payment = total_cost * portion_down_payment

while current_savings < down_payment:
    months = months + 1
    monthly_receive = current_savings * r/12
    current_savings += monthly_salary*portion_saved + monthly_receive
    
print('Number of months:'+str(months))