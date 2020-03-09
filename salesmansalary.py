#销售收入计算
#! /usr/bin/env python3
basic_salary = 1500
bonus_rate = 200
commission_rate = 0.02
numberofcamera = int(input("enter the number of camera:")
price = float(input("enter the camera price:")
bonus = (bonus_rate * numberofcamera)
commission = (commission_rate * price * numberofcamera)
print('Bonus        ={:6.2f}'.format(bonus))
print('Commission   ={:6.2f}'.format(commission))
print('Gross salary ={:6.2f}'.format(basic_salary + bonus + commission)
