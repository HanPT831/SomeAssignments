#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 21:37:07 2023
MIT 6.0001 ps1 part C
@author: hanpeitao
"""
months = 0
portion_down_payment = 0.25
current_savings = 0
r = 0.04
semi_annual_raise = .07
total_cost = 1000000
down_payment = total_cost * portion_down_payment
can_buy = True
right = 10000 
left = 0
portion_saved = right

counter = 0

print('Enter your annual salary:')
annual_salary = float(input())

while True:
    counter = counter + 1
    current_savings = 0
    monthly_salary = annual_salary/12
    portion_saved_dec = portion_saved /10000
    months=0
    while months <= 36:
        months += 1
        monthly_saving = monthly_salary*portion_saved_dec
        monthly_receive = (current_savings * r)/12
        current_savings += monthly_saving + monthly_receive
        if months%6 == 0:
            monthly_salary = monthly_salary * (1+semi_annual_raise)
    if abs(current_savings-down_payment)<=100:
        break
    if current_savings>down_payment:
        right = portion_saved
    else:
        left = portion_saved
    # print(left)
    # print(right)
    if left>=right:
        can_buy = False
        break
    portion_saved = (right+left)//2
if can_buy:
    print('Best savings rate: '+str(portion_saved_dec))
    print('Steps in bisection search: '+str(counter))
else:
    print('It is not possible to pay the down payment in three years.')

