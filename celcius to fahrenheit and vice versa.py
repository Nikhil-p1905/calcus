#-------------------------------------------------------------------------------
# Name:        Nikhil Kumar Sah
# Purpose:     Fahrenheit to celcius
#
# Author:      nikhil kr SAH
#
# Created:     28-09-2022
# Copyright:   (c) nikhil kr SAH 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Python program to convert temperature from celcius to fahrenheit and
#vice-versa.
#fahrenheit to celcius
t = float(input("Enter the fahrenheit : "))

c = (5/9)*(t-32)
print("fahrenheit to celcius : ",c)

#celcius to fahrenheit

t = float(input("Enter the celcius : "))
c = (9/5)*(t)+32
print("Celicius to Fahrenheit is : ",c)

